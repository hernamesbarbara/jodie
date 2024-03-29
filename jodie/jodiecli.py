#!/usr/bin/env python3
from jodie import Contact


def parse_args():
    # i'll add a command line tool later
    # for now this is just a stub / dummy data
    # similar to the way it'll look from docopt
    return {
        'first': 'John999999',
        'last': 'Doe99',
        'email': 'john99.doe99@example.com',
        'phone': '555-9999',
        'title': 'Software Engineer',
        'company': 'Tech Innovations Inc.',
        'website': 'https://www.tech-innovations.com'
    }


def main():
    data = parse_args()
    first, last, email, phone, title, company, website = data.values()

    contact = Contact(
        first,
        last,
        email,
        phone,
        title,
        company,
        website,
        note='foobar'
    )
    contact.save()


if __name__ == "__main__":
    main()
