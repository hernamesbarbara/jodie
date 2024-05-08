#!/usr/bin/env python3
# jodie/contact/contact.py
from datetime import datetime
import objc
from Contacts import (CNMutableContact, CNContactStore, CNSaveRequest, CNLabeledValue,
                      CNPhoneNumber, CNLabelURLAddressHomePage)
from Foundation import NSCalendar, NSDateComponents


def get_label_for_email(email):
    """
    Determine the label for an email address based on its domain.

    Args:
        email (str): The email address to analyze.

    Returns:
        str: "work" if the email domain is neither a common webmail provider nor an educational institution (.edu),
             otherwise "home".
    """
    webmail_providers = {
        "gmail.com", "googlemail.com", "aol.com", "yahoo.com",
        "hotmail.co.uk", "hotmail.com", "hotmail.de", "hotmail.es",
        "hotmail.fr", "hotmail.it", "hushmail.com", "protonmail.com",
        "hey.com", "icloud.com", "mac.com", "qq.com", "tuta.com",
        "tutanota.com", "verizon.net", "ymail.com"
    }

    # Extract the email's domain
    email_domain = email.split('@')[-1] if email else ""

    # Check domain against webmail providers and education domains (.edu)
    if email_domain not in webmail_providers and not email_domain.endswith('.edu'):
        return "work"
    else:
        return "home"


class Contact:
    """
    Simple wrapper for Apple iOS / macOS Contact record.
    """

    def __init__(self, first_name=None, last_name=None, email=None, phone=None, job_title=None, company=None, website=None, note=None):
        """
        Initialize a Contact object with optional parameters for various contact fields.

        Parameters:
            first_name (str, optional): First name of the contact.
            last_name (str, optional): Last name of the contact.
            email (str, optional): Email address of the contact.
            phone (str, optional): Phone number of the contact.
            job_title (str, optional): Job title of the contact.
            company (str, optional): Company name of the contact.
            website (str, optional): Website URL of the contact.
            note (str, optional): Additional notes for the contact.
        """
        self.contact = CNMutableContact.new()
        if first_name:
            self.first_name = first_name
        if last_name:
            self.last_name = last_name
        if email:
            self.email = email
        if phone:
            self.phone = phone
        if job_title:
            self.job_title = job_title
        if company:
            self.company = company
        if website:
            self.website = website
        if note and note.strip():
            self.note = note.strip()

        # Apple Contacts.app doesnt display created date by default
        # save the created date in a custom field
        self._created_date = datetime.now()
        self._set_creation_date()

    def _set_creation_date(self):
        """
        Set the creation date for the contact using the current date and store it as a custom date field.
        """
        dateComponents = NSDateComponents.alloc().init()
        dateComponents.setYear_(self._created_date.year)
        dateComponents.setMonth_(self._created_date.month)
        dateComponents.setDay_(self._created_date.day)
        customDateValue = CNLabeledValue.alloc().initWithLabel_value_(
            "created_date", dateComponents)
        self.contact.setDates_([customDateValue])

    def save(self):
        """
        Validate required fields and try to save to Contacts.app / Apple Address Book.
        """
        if not all([self.contact.givenName(), self.contact.familyName(), self.contact.emailAddresses()]):
            raise ValueError(
                "Missing required fields. First name, last name, and email are required.")

        store = CNContactStore.alloc().init()
        request = CNSaveRequest.alloc().init()
        request.addContact_toContainerWithIdentifier_(self.contact, None)

        error = objc.nil
        success, error = store.executeSaveRequest_error_(request, None)
        if not success:
            raise Exception(f"Failed to save contact: {error}")
        return self

    def __str__(self):
        return (f"Contact: {self.first_name} {self.last_name}, "
                f"Email: {self.email}, Phone: {self.phone}, "
                f"Job Title: {self.job_title}, Company: {self.company}, "
                f"Website: {self.website}")

    def __repr__(self):
        """
        Return an unambiguous string representation of the contact,
        potentially usable for recreating the object.
        """
        return (f"{self.__class__.__name__}(first_name={self.first_name!r}, "
                f"last_name={self.last_name!r}, email={self.email!r}, "
                f"phone={self.phone!r}, job_title={self.job_title!r}, "
                f"company={self.company!r}, website={self.website!r})")

    @property
    def first_name(self):
        return self.contact.givenName()

    @first_name.setter
    def first_name(self, value):
        self.contact.setGivenName_(value.strip().title())

    @property
    def last_name(self):
        return self.contact.familyName()

    @last_name.setter
    def last_name(self, value):
        self.contact.setFamilyName_(value.strip().title())

    @property
    def email(self):
        emailAddresses = self.contact.emailAddresses()
        return emailAddresses[0].value() if emailAddresses else None

    @email.setter
    def email(self, value):
        email_label = get_label_for_email(value)
        emailValue = CNLabeledValue.alloc().initWithLabel_value_(
            email_label, value.strip().lower())
        self.contact.setEmailAddresses_([emailValue])

    @property
    def phone(self):
        phoneNumbers = self.contact.phoneNumbers()
        return phoneNumbers[0].value().stringValue() if phoneNumbers else None

    @phone.setter
    def phone(self, value):
        # Remove all unwanted characters, but keep digits and plus sign
        cleaned_number = ''.join(
            ch for ch in value if ch.isdigit() or ch == '+')

        label = "mobile"

        # Create the CNPhoneNumber object
        phone_number = CNPhoneNumber.phoneNumberWithStringValue_(
            cleaned_number)

        # Create the labeled value
        phone_label_value = CNLabeledValue.alloc().initWithLabel_value_(
            label, phone_number)

        # Set the phone number with the new labeled value
        self.contact.setPhoneNumbers_([phone_label_value])

    @property
    def job_title(self):
        return self.contact.jobTitle()

    @job_title.setter
    def job_title(self, value):
        self.contact.setJobTitle_(value.strip().title())

    @property
    def company(self):
        return self.contact.organizationName()

    @company.setter
    def company(self, value):
        self.contact.setOrganizationName_(value.strip().title())

    @property
    def website(self):
        urlAddresses = self.contact.urlAddresses()
        return urlAddresses[0].value() if urlAddresses else None

    @website.setter
    def website(self, value):
        if value:
            websiteValue = CNLabeledValue.alloc().initWithLabel_value_(
                CNLabelURLAddressHomePage, value.strip().lower())
            self.contact.setUrlAddresses_([websiteValue])
        else:
            self.contact.setUrlAddresses_([])

    @property
    def note(self):
        return self.contact.note()

    @note.setter
    def note(self, value):
        self.contact.setNote_(value.strip())
