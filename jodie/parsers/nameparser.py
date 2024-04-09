#!/usr/bin/env python3
# jodie/parsers/nameparser.py
from .baseparser import BaseParser
from .emailparser import EmailParser


class NameParser(BaseParser):
    @classmethod
    def parse(cls, text):
        email = EmailParser.parse(text)

        # If an email is found, use the part of the text before the email for name parsing.
        # e.g. John von Doe99 <john.vondoe99@gmail.com>
        # this will find the email and assume the left hand side of the email is the full name
        if email:
            # Find the part before the email address; remove the angled brackets if they are present.
            name_portion_index = text.find(email)
            name_portion = text[:name_portion_index].strip()
            # Further cleaning to remove any leading/trailing special characters that might have been part of the email format.
            name_portion = name_portion.rstrip('<').rstrip().title()
        else:
            # If no email is found, use the entire text as the name portion.
            name_portion = text.strip().title()

        if not name_portion:
            return "", ""

        words = name_portion.split()

        first_name = words[0] if words else ""

        if len(words) > 1:
            last_name = " ".join(words[1:])  # Join the last name
            last_name = last_name[:255]  # Truncate if longer than 255 chars
        else:
            last_name = ""

        return first_name, last_name
