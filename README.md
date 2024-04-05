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

```

### Build the package with the `build` package and install with either `pip` or `PyInstaller`.

```
python -m build
pip install .

```

### Build with PyInstaller

**TODO**

I'm working on a homebrew tap to allow you to install `jodie` with homebrew.

Seems like the only way to be able to sign the code with Apple entitlements for interacting with Contacts.app.
