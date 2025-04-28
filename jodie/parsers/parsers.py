#!/usr/bin/env python3
# jodie/parsers/parsers.py
import re
from nameparser import HumanName

class BaseParser:
    """
    Base class for parsing text into specific contact properties.
    """

    def __init__(self):
        pass

    @staticmethod
    def find_matches(pattern, text):
        """
        Find all matches of a regex pattern in the given text.

        :param pattern: Regex pattern to match against the text.
        :param text: The text to search in.
        :return: A list of all matches.
        """
        return re.findall(pattern, text)

    @classmethod
    def parse(cls, text):
        """
        Parse the given text to extract information.
        This method should be implemented by subclasses.

        :param text: The text to parse.
        :return: Extracted information.
        """
        raise NotImplementedError("Subclasses must implement this method.")


class EmailParser(BaseParser):
    @classmethod
    def parse(cls, text):
        """
        Extracts a single email from the text.
        Returns the first valid match or None.
        """
        email_pattern = r'<(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b)>' \
                        r'|(\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b)'
        matches = cls.find_matches(email_pattern, text)
        for match in matches:
            # Return the first non-empty match
            if isinstance(match, tuple):
                return next((item for item in match if item), None)
            return match
        return None


class TitleParser(BaseParser):
    # Extend COMMON_TITLES with dataset insights
    COMMON_TITLES = {
        "ceo", "cto", "co-founder", "founder", "director", "manager", "engineer",
        "president", "vice-president", "consultant", "advisor", "chief",
        "specialist", "developer", "partner", "head", "lead", "co-ceo"
    }

    @classmethod
    def parse(cls, text):
        """
        Enhanced title parsing:
        - Standardizes capitalization for common titles.
        """
        if not isinstance(text, str) or not text.strip():
            return None

        # Normalize text
        cleaned_text = text.strip().lower()

        # Match against common titles
        if cleaned_text in cls.COMMON_TITLES:
            return cleaned_text.upper()  # Standardize capitalization

        return None



class WebsiteParser(BaseParser):
    @classmethod
    def parse(cls, text):
        # Match typical URL patterns
        url_pattern = r'https?://[^\s]+|www\.[^\s]+'
        urls = cls.find_matches(url_pattern, text)
        return urls[0] if urls else None


class NameParser(BaseParser):
    @classmethod
    def parse(cls, text):
        """
        Parse a name from the given text.
        - If an email is present in mailbox format, extract the portion before the email.
        - Use the `nameparser` package to parse the extracted name.

        :param text: The text to parse.
        :return: A tuple of (first_name, last_name).
        """
        # Check for email in the text.
        email = EmailParser.parse(text)
        if email:
            # Extract the portion of text before the email for name parsing.
            name_portion_index = text.find(email)
            name_portion = text[:name_portion_index].strip()
            name_portion = name_portion.rstrip('<').strip()
        else:
            # Use the entire text if no email is found.
            name_portion = text.strip()

        if not name_portion:
            return "", ""

        # Use the `HumanName` class to parse the name intelligently.
        name = HumanName(name_portion)

        # Return the first and last names as a tuple.
        return name.first, f"{name.middle} {name.last}".strip()
