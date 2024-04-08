#!/usr/bin/env python3
import re


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
