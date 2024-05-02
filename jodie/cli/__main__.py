#!/usr/bin/env python3
# jodie/cli/__main__.py
import sys
from docopt import docopt
import jodie

COMMANDS = ('new', 'parse',)
NOT_ARGS = ('--help', '--version',)

__doc__ = """jodie - Manage macOS Contacts.app from command line!

Usage: 
    jodie new [EMAIL NAME COMPANY TITLE NOTES...]
    jodie new [options]
    jodie parse [options] TEXT

Arguments:
    EMAIL                               Email address for the contact you want to create.
    NAME                                Full name for the contact you want to create.
    COMPANY                             Company name.
    TITLE                               Job title.
    NOTES                               Any text you want to save in the `Note` field in Contacts.app.
    TEXT                                Text for jodie to try her best to parse semi-intelligently if she can.

Options:
    -C COMPANY --company=COMPANY        Company name.
    -E EMAIL --email=EMAIL              Email.
    -F FIRST --first=FIRST              First name.
    -L LAST --last=LAST                 Last name.
    -N NOTES --notes=NOTES              Any text you want to save in the `Note` field in Contacts.app.
    -P PHONE --phone=PHONE              Phone.
    -T TITLE --title=TITLE              Job title.
    -X TEXT  --text=TEXT                Text for jodie to try her best to parse semi-intelligently if she can.
    -U NAME --full-name=NAME            Full name.
    -W WEBSITE --website=WEBSITE        Website / URL.
    -H --help                           Show this screen.
    -V --version                        Show version.

"""


def detect_argument_mode(args):
    """
    Determines if the command was called with named options or positional arguments.
    Named options are identified by the presence of any specific options set.
    Assumes any presence of non-help/version named options indicates 'named' mode.
    """
    if any(args.get(arg) for arg in NOT_ARGS):
        return "positional"  # Early return if help or version is called

    # Identify if any specific named options are used
    named_options = {key: args[key] for key in args.keys(
    ) if key.startswith('--') and key not in NOT_ARGS}
    return "named" if any(named_options.values()) else "positional"


def main():
    args = docopt(__doc__, version=jodie.__version__)

    mode = detect_argument_mode(args)
    # Assuming 'args' is the dictionary returned by docopt
    if mode == "positional":
        try:
            # The name should be a single string. Ensure it's being treated as such.
            full_name = args['NAME']
            first, last = jodie.parsers.NameParser.parse(full_name)
            email = jodie.parsers.EmailParser.parse(args['EMAIL'])
        except Exception as e:
            sys.stderr.write(
                f"Error processing positional arguments: {str(e)}\n")
            sys.exit(1)
        company = args.get('COMPANY')
        title = args.get('TITLE')
        notes = args.get('NOTES')

    elif mode == "named":
        try:
            first = args.get('--first')
            last = args.get('--last')
            email = args.get('--email')
            company = args.get('--company')
            title = args.get('--title')
            notes = args.get('--notes')
        except Exception as e:
            sys.stderr.write(f"Error processing named arguments: {str(e)}\n")
            sys.exit(1)

    c = jodie.contact.Contact(
        first_name=first, last_name=last, email=email, company=company, job_title=title)
    sys.stdout.write(f'Saving...\n{c}\n')
    status = 0 if c.save() else 1
    sys.exit(status)


if __name__ == "__main__":
    main()
