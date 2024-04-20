#!/usr/bin/env python3
# jodie/cli/__main__.py
import sys
import docopt
import jodie

args = {
    'first': 'John999999',
    'last': 'Doe99',
    'email': 'john99.doe99@example.com',
    'phone': '555-9999',
    'title': 'Software Engineer',
    'company': 'Tech Innovations Inc.',
    'website': 'https://www.tech-innovations.com'
}


# def main():
#     print('Got here: jodie/cli/main:run()')
#     print('__doc__', jodie.cli.__doc__)
#     first, last, email, phone, title, company, website = args.values()

#     c = jodie.contact.Contact(
#         first,
#         last,
#         email,
#         phone,
#         title,
#         company,
#         website,
#         note='foobar'
#     )
#     print(c)

def main():
    args = docopt.docopt(jodie.cli.__doc__, version=jodie.__version__)

    # if no parsing options specified explicitly, try to parse everything
    options = {k: v for k, v in args.items() if k not in ('--all', 'TEXT')}
    if not any(v for v in options.values()):
        args['--all'] = True
    if args.get('--all', False):
        for k in options:
            args[k] = True

    sys.exit(args)


if __name__ == "__main__":
    main()
