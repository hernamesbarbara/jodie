#!/usr/bin/env python3
from .baseparser import BaseParser


class EmailParser(BaseParser):
    @classmethod
    def parse(cls, text):
        # email regex should handle with or without angled brackets
        # e.g. John von Doe99 <john.vondoe99@gmail.com> or John von Doe99 john.vondoe99@gmail.com
        email_pattern = r'<?(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b)>?'
        emails = cls.find_matches(email_pattern, text)
        return emails[0] if emails else None
