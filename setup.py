#!/usr/bin/env python3
import os
import re
from setuptools import setup, find_packages

def extract_version_from_script(fname):
    """
    Attempts to find the version number in the file named fname. Allows for spaces around 
    the equals sign. Raises RuntimeError if version number of file is not found.
    """
    version = ""
    base_dir = os.path.dirname(os.path.abspath(__file__))
    fname = os.path.join(base_dir, fname)
    
    reg = re.compile(r"__version__\s*=\s*[\""]([^\""]+)[\""]")
    
    with open(fname, "r") as fp:
        for line in fp:
            m = reg.search(line)
            if m:
                version = m.group(1)
                break
    
    if not version:
        raise RuntimeError(f"Cannot find version information in {fname}")
    
    return version

NAME = "Jodie"
VERSION = extract_version_from_script("jodie/__init__.py")
PACKAGES = find_packages()
CONSOLE_SCRIPTS = ["jodie=jodie.__main__:run"]

config = {
    "name": "jodie",
    "description": "Jodie lets you add contacts to Contacts.app on macOS from command line",
    "author": "austin",
    "keywords": "macOS Contacts.app command line tool.",
    "author_email": "tips@cia.lol",
    "version": VERSION,
    "install_requires": [],
    "packages": PACKAGES,
    "license": "MIT",
    "entry_points": {"console_scripts": CONSOLE_SCRIPTS},
    "setup_requires": []
}

setup(**config)
