## Jodie is a command line tool to quickly save new contacts to Contacts.app on macOS

save macOS contacts to Apple's Contacts.app from command line.

`Jodie` is named for for [Jodie Foster](https://en.wikipedia.org/wiki/Jodie_Foster) for her stellar performance in the movie[ Contact](<https://en.wikipedia.org/wiki/Contact_(1997_American_film)>).

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

###

#### Build `jodie` executable with Apple entitlements

```
# clone the repo
# run the pyinstaller build script
# you will need to get an Apple developer application certificate
# and update the build script accordingly for this to work
# this is how you grant all the privileges to `jodie` for accessing Contacts.app


# this build script will save and sign `dist/jodie` executable
./pyinstaller-build/pyinstaller-build.sh


```
