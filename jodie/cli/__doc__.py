#!/usr/bin/env python3
# jodie/cli/__doc__.py
"""jodie - Manage macOS Contacts.app from command line!

Usage: 
    jodie new [EMAIL NAME COMPANY TITLE NOTE...]
    jodie new [options]
    jodie parse [options] TEXT

Arguments:
    EMAIL                               Email address for the contact you want to create.
    NAME                                Full name for the contact you want to create.
    COMPANY                             Company name.
    TITLE                               Job title.
    NOTE                                Any text you want to save in the `Note` field in Contacts.app.
    TEXT                                Text for jodie to try her best to parse semi-intelligently if she can.

Options:
    -C COMPANY --company=COMPANY        Company name.
    -E EMAIL --email=EMAIL              Email.
    -F FIRST --first=FIRST              First name.
    -L LAST --last=LAST                 Last name.
    -U NAME --full-name=NAME            Full name.
    -N NOTE --note=NOTE                 Any text you want to save in the `Note` field in Contacts.app.
    -P PHONE --phone=PHONE              Phone.
    -T TITLE --title=TITLE              Job title.
    -X TEXT  --text=TEXT                Text for jodie to try her best to parse semi-intelligently if she can.    
    -W WEBSITE --website=WEBSITE        Website / URL.
    -H --help                           Show this screen.
    -V --version                        Show version.

"""
