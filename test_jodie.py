#!/usr/bin/env python3
# test_jodie.py
import jodie


def parse_args(which=1):
    """
    i'll add a command line tool later for now this is just 
    a stub / dummy data similar to the way it'll look from docopt
    """

    if which == 1:
        return {
            '--company': False,
            '--defaults': True,
            '--email': True,
            '--first': False,
            '--help': False,
            '--last': False,
            '--name': True,
            '--phone': False,
            '--title': False,
            '--version': False,
            '--website': False,
            'EMAIL': None,
            'NAME': [],
            'TEXT': 'john99 Doe9999 <john99.Doe9999@Gmail.com>'
        }

    else:
        return {
            '--company': False,
            '--defaults': False,
            '--email': False,
            '--first': False,
            '--help': False,
            '--last': False,
            '--name': False,
            '--phone': False,
            '--title': False,
            '--version': False,
            '--website': False,
            'EMAIL': 'john99.Doe9999@Gmail.com',
            'NAME': ['john99', 'doe9999'],
            'TEXT': None
        }


# raw_text = "John von Doe99 <john.vondoe99@gmail.com>"
# print(jodie.parsers.NameParser.parse(raw_text))

# print(jodie.parsers.EmailParser.parse(raw_text))

# print(jodie.parsers.NameParser.parse(f"this is random text {raw_text}"))

# data = parse_args()
# first, last, email, phone, title, company, website = data.values()

args = parse_args(1)

if args.get('EMAIL') and args.get('NAME'):
    print('if block')
    full_name = " ".join(args["NAME"])
    first, last = jodie.parsers.NameParser.parse(full_name)
    email = jodie.parsers.EmailParser.parse(args['EMAIL'])
else:
    print('else block')
    first, last = jodie.parsers.NameParser.parse(args['TEXT'])
    email = jodie.parsers.EmailParser.parse(args['TEXT'])


# first, last = jodie.parsers.NameParser.parse(args['TEXT'])
# email = jodie.parsers.EmailParser.parse(args['TEXT'])


c = jodie.contact.Contact(first_name=first, last_name=last, email=email)
