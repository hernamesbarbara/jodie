## Jodie is a command line tool to quickly save new contacts to Contacts.app on macOS

this is a work in progress.

basically it's a python wrapper around Apple's `objc` python package.

### install

Clone the repo and install with `pip`

```
pip install .
```

then test that you can run the `jodie` command

```
jodie
```

or

```
python -m jodie.jodiecli
```

### TODO

- hook up docopt arg parsing
- get rid of the stub / mock data from parse_args
- figure out how to save `note` value on the contact record in apple contacts
- probably need to bundle the whole project as an Apple macOS app to get security and privacy entitlement to read/write to that field

https://developer.apple.com/documentation/bundleresources/entitlements/com_apple_developer_contacts_notes
