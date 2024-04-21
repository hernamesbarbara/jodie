## Jodie is a command line tool to quickly save new contacts to Contacts.app on macOS

Save macOS contacts to Apple's Contacts.app from command line.

`Jodie` is named for for [Jodie Foster](https://en.wikipedia.org/wiki/Jodie_Foster) for her stellar performance in the movie[ Contact](<https://en.wikipedia.org/wiki/Contact_(1997_American_film)>).

this is a work in progress.

## Installation

Clone the repo from Github: [hernamesbarbara/jodie](https://github.com/hernamesbarbara/jodie)

```
# Clone the repo
git clone git@github.com:hernamesbarbara/jodie.git
cd jodie/
pip install .
```

#### Test that you have the CLI installed

```
~ jodie --help
jodie.

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

```

#### Save a new Contact to macOS Address Book / Contacts.app

```
jodie john99.doe999@gmail.com John99 von Doe99
Saving...
Contact: John99 Von Doe99, Email: john99.doe999@gmail.com, Phone: None, Job Title: , Company: , Website: None
Contact saved successfully!

```
