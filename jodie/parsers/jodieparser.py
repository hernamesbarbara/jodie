#!/usr/bin/env python3

from .baseparser import BaseParser
from .nameparser import NameParser
from .emailparser import EmailParser


class JodieParser(BaseParser):
    @classmethod
    def parse(cls, text):
        contact_info = {}
        contact_info['email'] = EmailParser.parse(text)
        first_name, last_name = NameParser.parse(text)
        if first_name and last_name:
            contact_info['first_name'] = first_name
            contact_info['last_name'] = last_name

        return contact_info
