#!/usr/bin/env python3
# jodie/cli/__main__.py
import sys
import docopt
import jodie


def main():
    args = docopt.docopt(jodie.cli.__doc__, version=jodie.__version__)

    non_options = ('--help', '--version', '--defaults', 'TEXT',)

    # if no parsing options specified explicitly, try to parse everything
    options = {k: v for k, v in args.items() if k not in non_options}

    if not any(v for v in options.values()):
        args['--defaults'] = True
    if args.get('--defaults', False):
        for k in options:
            if k in jodie.cli.DEFAULT_FIELDS:
                args[k] = True

    if args.get('EMAIL') and args.get('NAME'):
        full_name = " ".join(args["NAME"])
        first, last = jodie.parsers.NameParser.parse(full_name)
        email = jodie.parsers.EmailParser.parse(args['EMAIL'])

    elif args.get('TEXT'):
        first, last = jodie.parsers.NameParser.parse(args['TEXT'])
        email = jodie.parsers.EmailParser.parse(args['TEXT'])
    else:
        sys.stderr.write('Something went wrong...unable to parse arguments\n')
        sys.exit(1)

    c = jodie.contact.Contact(first_name=first, last_name=last, email=email)
    sys.stdout.write(f'Saving...\n{c}\n')
    status = 0 if c.save() else 1
    if status == 0:
        sys.stdout.write('Contact saved successfully!\n')
    else:
        sys.stderr.write(
            'Something went wrong while trying to save contact.\n')
    sys.exit(status)


if __name__ == "__main__":
    # EXAMPLE call
    # python -m jodie.cli "John99 Doe999 <john99.doe9999@gmail.com>"
    # python -m jodie.cli john99.doe9999@gmail.com john99 doe9999
    main()
