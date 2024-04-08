#!/usr/bin/env python3
# test_jodie.py
import jodie


def parse_args():
    """
    i'll add a command line tool later for now this is just 
    a stub / dummy data similar to the way it'll look from docopt
    """

    return {
        'first': 'John999999',
        'last': 'Doe99',
        'email': 'john99.doe99@example.com',
        'phone': '555-9999',
        'title': 'Software Engineer',
        'company': 'Tech Innovations Inc.',
        'website': 'https://www.tech-innovations.com'
    }


raw_text = "John von Doe99 <john.vondoe99@gmail.com>"
print(jodie.parsers.NameParser.parse(raw_text))

print(jodie.parsers.EmailParser.parse(raw_text))
print(jodie.parsers.JodieParser.parse(raw_text))

print(jodie.parsers.NameParser.parse(f"this is random text {raw_text}"))
