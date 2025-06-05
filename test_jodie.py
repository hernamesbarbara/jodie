#!/usr/bin/env python3
# test_jodie.py
import jodie
import unittest
from jodie.cli.__main__ import parse_auto  # Import parse_auto directly


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
            '--websites': False,
            '--note': False,
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
            '--websites': False,
            '--note': False,
            'EMAIL': 'john99.Doe9999@Gmail.com',
            'NAME': ['john99', 'doe9999'],
            'TEXT': None
        }


class TestJodie(unittest.TestCase):
    def test_parsing_order(self):
        """Test that fields are parsed in the correct order with proper precedence."""
        # Test case with all fields to verify parsing order
        text = [
            "sarah@acme.com",  # email
            "https://linkedin.com/in/sarah",  # website
            "Senior Software Engineer",  # job title
            "Sarah Smith",  # name
            "Acme Inc"  # company
        ]
        
        fields = parse_auto(text)
        
        # Verify each field was parsed correctly
        self.assertEqual(fields["email"], "sarah@acme.com")
        self.assertEqual(len(fields["websites"]), 1)
        self.assertEqual(fields["job_title"], "Senior Software Engineer")
        self.assertEqual(fields["first_name"], "Sarah")
        self.assertEqual(fields["last_name"], "Smith")
        self.assertEqual(fields["company"], "Acme Inc")

    def test_job_title_detection(self):
        """Test enhanced job title detection."""
        test_cases = [
            ("CEO", "CEO"),
            ("Senior Software Engineer", "Senior Software Engineer"),
            ("Lead Product Manager", "Lead Product Manager"),
            ("VP of Engineering", "VP of Engineering"),
            ("Not a title", None)
        ]
        
        for input_title, expected in test_cases:
            result = jodie.parsers.TitleParser.parse(input_title)
            self.assertEqual(result, expected, f"Failed to parse title: {input_title}")

    def test_missing_values(self):
        """Test consistent handling of missing values."""
        # Test with empty strings and whitespace
        contact = jodie.contact.Contact(
            first_name="",
            last_name="   ",
            email="test@example.com",
            job_title="",
            company=None
        )
        
        # Verify empty values are not set
        self.assertIsNone(contact.first_name)
        self.assertIsNone(contact.last_name)
        self.assertEqual(contact.email, "test@example.com")
        self.assertIsNone(contact.job_title)
        self.assertIsNone(contact.company)

    def test_company_fallback(self):
        """Test company name fallback behavior."""
        # Test case where company name could be confused with other fields
        text = [
            "john@example.com",
            "https://example.com",
            "CEO",
            "John Doe",
            "Example Technologies"  # Should be company, not job title
        ]
        
        fields = parse_auto(text)
        
        # Verify company is set correctly and not confused with job title
        self.assertEqual(fields["job_title"], "CEO")
        self.assertEqual(fields["company"], "Example Technologies")

    def test_compound_fields(self):
        """Test handling of compound fields and edge cases."""
        text = [
            "john.smith@acme.com",
            "https://github.com/johnsmith",
            "https://linkedin.com/in/johnsmith",
            "Senior Full Stack Engineer",
            "John A. Smith",
            "Acme Technologies Inc"
        ]
        
        fields = parse_auto(text)
        
        # Verify compound fields are handled correctly
        self.assertEqual(fields["email"], "john.smith@acme.com")
        self.assertEqual(len(fields["websites"]), 2)
        self.assertEqual(fields["job_title"], "Senior Full Stack Engineer")
        self.assertEqual(fields["first_name"], "John")
        self.assertEqual(fields["last_name"], "A. Smith")
        self.assertEqual(fields["company"], "Acme Technologies Inc")


if __name__ == "__main__":
    unittest.main()
