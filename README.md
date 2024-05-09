## Jodie is a command line tool to quickly save new contacts to Contacts.app on macOS

Save macOS contacts to Apple's Contacts.app from command line.

`Jodie` is named for for [Jodie Foster](https://en.wikipedia.org/wiki/Jodie_Foster) for her stellar performance in the movie[ Contact](<https://en.wikipedia.org/wiki/Contact_(1997_American_film)>).

this is a work in progress.

## Installation

clone 

```
# Clone the repo
git clone git@github.com:hernamesbarbara/jodie.git
cd jodie/
pip install .
```

#### Usage

```
jodie-cli --help
jodie - Manage macOS Contacts.app from command line!

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
    -N NOTE --note=NOTE                 Any text you want to save in the `Note` field in Contacts.app.
    -P PHONE --phone=PHONE              Phone.
    -T TITLE --title=TITLE              Job title.
    -X TEXT  --text=TEXT                Text for jodie to try her best to parse semi-intelligently if she can.
    -U NAME --full-name=NAME            Full name.
    -W WEBSITE --website=WEBSITE        Website / URL.
    -H --help                           Show this screen.
    -V --version                        Show version.

```

#### Save a new Contact to macOS Address Book / Contacts.app

```
jodie-cli new \
    --email "john99.doe99@gmail.com" \
    --first john99 \
    --last doe99 \
    --company "AcmeCo Inc" \
    --title "Founder" \
    --website "https://example.com" \
    --phone "+1 555 555 5555"

```
