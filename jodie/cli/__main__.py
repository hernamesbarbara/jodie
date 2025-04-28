#!/usr/bin/env python3
# jodie/cli/__main__.py
import sys
from docopt import docopt
from nameparser import HumanName
import jodie
from jodie.cli.__doc__ import __version__, __description__, __url__, __doc__

COMMANDS = ('new', 'parse',)
NOT_ARGS = ('--help', '--version', '--auto')

def detect_argument_mode(args):
    """
    Determines the mode based on provided arguments:
    - "auto": if --auto is specified.
    - "named": if named arguments are provided.
    - "positional": if positional arguments are used.
    """
    if args['--auto']:
        return "auto"
    if any(args.get(arg) for arg in NOT_ARGS if arg != '--auto'):
        return "positional"
    
    named_options = {}
    for key in args.keys():
        if key.startswith('--') and key not in NOT_ARGS:
            named_options[key] = args[key]

    if any(named_options.values()):
        return "named" 
    return "positional"

def parse_auto(arguments):
    detected_fields = {
        "first_name": None,
        "last_name": None,
        "email": None,
        "phone": None,
        "job_title": None,
        "company": None,
        "websites": None,
        "note": None
    }

    for arg in arguments:
        # Check for email first.
        if not detected_fields["email"]:
            email = jodie.parsers.EmailParser.parse(arg)
            if email:
                detected_fields["email"] = email
                # Infer name from mailbox format if name is not already set
                if not detected_fields["first_name"]:
                    first_name, last_name = jodie.parsers.NameParser.parse(arg)
                    if first_name or last_name:
                        detected_fields["first_name"] = first_name
                        detected_fields["last_name"] = last_name
                continue

        # Check for website.
        if not detected_fields["websites"]:
            website = jodie.parsers.WebsiteParser.parse(arg)
            if website:
                detected_fields["websites"] = website
                continue

        # Check for company only if it's not already set.
        if not detected_fields["company"]:
            if "inc" in arg.lower() or "llc" in arg.lower():
                detected_fields["company"] = arg.strip()
                continue

        # Check for title only if it's not already set.
        if not detected_fields["job_title"]:
            title = jodie.parsers.TitleParser.parse(arg)
            if title:
                detected_fields["job_title"] = title
                continue

        # Check for name only if it's not already set.
        if not detected_fields["first_name"]:
            first_name, last_name = jodie.parsers.NameParser.parse(arg)
            if first_name or last_name:
                detected_fields["first_name"] = first_name
                detected_fields["last_name"] = last_name
                continue

        # Fallback for unclassified arguments.
        if not detected_fields["company"]:
            detected_fields["company"] = arg
        else:
            print(f"Unclassified argument: {arg}")  # Log for debugging.
            detected_fields["company"] = 'JODIE: UNK'

    return detected_fields


def main():
    first, last, email, phone, title, company, websites, note = (None,) * 8

    args = docopt(__doc__, version=__version__)
    mode = detect_argument_mode(args)

    if mode == "auto":
        fields = parse_auto(args['TEXT'])
        if fields:
            if fields.get('first_name'):
                human_name = HumanName(f"{fields['first_name']} {fields['last_name']}".strip())
                if human_name:
                    first, last = human_name.first, human_name.last
            
            email = fields.get('email')
            phone = fields.get('phone')
            title = fields.get('job_title')
            company = fields.get('company')
            websites = fields.get('websites')
            if websites:
                # Split the comma-separated list of websites
                websites = [url.strip() for url in websites.split(',')]
            note = fields.get('note')

    if mode == "positional":
        try:
            full_name = args['NAME']
            first, last = jodie.parsers.NameParser.parse(full_name)
            email = jodie.parsers.EmailParser.parse(args['EMAIL'])
        except Exception as e:
            sys.stderr.write(
                f"Error processing positional arguments: {str(e)}\n")
            sys.exit(1)
        company = args.get('COMPANY')
        title = args.get('TITLE')
        note = args.get('NOTE')

    elif mode == "named":
        try:
            first = args.get('--first')
            last = args.get('--last')
            full = args.get('--full-name')
            if full:
                parts = full.split()
                if first is None:
                    first = parts[0].strip()
                if last is None:
                    last = ' '.join(parts[1:]).strip()
            email = args.get('--email')
            phone = args.get('--phone')
            title = args.get('--title')
            company = args.get('--company')
            websites = args.get('--websites')
            if websites:
                # Split the comma-separated list of websites
                websites = [url.strip() for url in websites.split(',')]
            note = args.get('--note')

        except Exception as e:
            sys.stderr.write(f"Error processing named arguments: {str(e)}\n")
            sys.exit(1)

    c = jodie.contact.Contact(
        first_name=first,
        last_name=last,
        email=email,
        phone=phone,
        job_title=title,
        company=company,
        websites=websites
        # note=note
    )

    sys.stdout.write(f'Saving...\n{c}\n')
    status = 0 if c.save() else 1
    sys.exit(status)


if __name__ == "__main__":
    main()
