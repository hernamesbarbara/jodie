#!/usr/bin/env python3
# jodie/cli/__init__.py

DEFAULT_FIELDS = ('--name', '--email',)

__doc__ = """jodie.

Usage: 
    jodie [options] TEXT
    jodie [options] EMAIL NAME...

Arguments:
    TEXT                   Text you want jodie to attempt to parse contact information from.
    EMAIL                  Email address for the contact you want to create.
    NAME                   Full name for the contact you want to create.

Options:
    -D --defaults          Try to parse all default contact fields. [default: True]
    -N --name              Full name of the user. [default: True]
    -F --first             First name of the user.
    -L --last              Last name of the user.
    -E --email             Email address of the user. [default: True]
    -P --phone             Phone number of the user.
    -T --title             Job title of the user.
    -C --company           Company name where the user is employed.
    -W --website           Website URL of the company.
    -H --help              Show this screen.
    -V --version           Show version.

"""
