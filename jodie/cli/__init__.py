#!/usr/bin/env python3
# jodie/cli/__init__.py

__doc__ = """jodie.

Usage: 
    jodie [options] TEXT

Arguments:
    TEXT                   Text you want jodie to attempt to parse contact information from.

Options:
    -A --all               Try to parse all contact information you can find. [Default: True]
    -N --name              Full name of the user.
    -F --first             First name of the user.
    -L --last              Last name of the user.
    -E --email             Email address of the user.
    -P --phone             Phone number of the user.
    -T --title             Job title of the user.
    -C --company           Company name where the user is employed.
    -W --website           Website URL of the company.
    -H --help              Show this screen.
    -V --version           Show version.

"""

__all__ = ("main", "__doc__")
