#!/usr/bin/env python3
# jodie/contact/contact.py
from datetime import datetime
import objc
from Contacts import (CNMutableContact, CNContactStore, CNSaveRequest, CNLabeledValue,
                      CNPhoneNumber, CNLabelURLAddressHomePage)
from Foundation import NSCalendar, NSDateComponents


class Contact:
    """
    Simple wrapper for Apple iOS / macOS Contact record.
    """

    def __init__(self, first_name, last_name, email, phone, job_title, company, website, note=""):
        """
        Initialize a Contact object with the given parameters.

        Parameters:
            first_name (str)
            last_name (str)
            email (str): Valid email address.
            phone (str): Phone number, can include punctuation and/or spaces.
            job_title (str)
            company (str)
            website (str)
            note (str, optional): Additional note for the contact. Defaults to an empty string.
        """
        self.contact = CNMutableContact.new()
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone = phone
        self.job_title = job_title
        self.company = company
        self.website = website
        # Note handling is omitted as it's noted to be currently problematic.

        # Apple Contacts.app doesnt display created date by default
        # save the created date in a custom field
        self._set_creation_date()

    def save(self):
        """
        Try to save the contact to the Apple address book.
        """
        store = CNContactStore.alloc().init()
        request = CNSaveRequest.alloc().init()
        request.addContact_toContainerWithIdentifier_(self.contact, None)

        error = objc.nil
        success, error = store.executeSaveRequest_error_(request, None)
        if not success:
            print(f"Failed to save contact: {error}")
        else:
            print("Contact saved successfully.")

    def _set_creation_date(self):
        """
        Set the creation date for the contact using the current date.
        """
        today = datetime.now()
        dateComponents = NSDateComponents.alloc().init()
        dateComponents.setYear_(today.year)
        dateComponents.setMonth_(today.month)
        dateComponents.setDay_(today.day)
        customDateValue = CNLabeledValue.alloc().initWithLabel_value_(
            "created_date", dateComponents)
        self.contact.setDates_([customDateValue])

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
        self.contact.setGivenName_(value)

    @property
    def last_name(self):
        return self.contact.familyName()

    @last_name.setter
    def last_name(self, value):
        self.contact.setFamilyName_(value)

    @property
    def email(self):
        emailAddresses = self.contact.emailAddresses()
        return emailAddresses[0].value() if emailAddresses else None

    @email.setter
    def email(self, value):
        emailValue = CNLabeledValue.alloc().initWithLabel_value_("work", value)
        self.contact.setEmailAddresses_([emailValue])

    @property
    def phone(self):
        phoneNumbers = self.contact.phoneNumbers()
        return phoneNumbers[0].value().stringValue() if phoneNumbers else None

    @phone.setter
    def phone(self, value):
        phoneValue = CNLabeledValue.alloc().initWithLabel_value_(
            "mobile", CNPhoneNumber.phoneNumberWithStringValue_(value))
        self.contact.setPhoneNumbers_([phoneValue])

    @property
    def job_title(self):
        return self.contact.jobTitle()

    @job_title.setter
    def job_title(self, value):
        self.contact.setJobTitle_(value)

    @property
    def company(self):
        return self.contact.organizationName()

    @company.setter
    def company(self, value):
        self.contact.setOrganizationName_(value)

    @property
    def website(self):
        urlAddresses = self.contact.urlAddresses()
        return urlAddresses[0].value() if urlAddresses else None

    @website.setter
    def website(self, value):
        if value:
            websiteValue = CNLabeledValue.alloc().initWithLabel_value_(
                CNLabelURLAddressHomePage, value)
            self.contact.setUrlAddresses_([websiteValue])
        else:
            self.contact.setUrlAddresses_([])
