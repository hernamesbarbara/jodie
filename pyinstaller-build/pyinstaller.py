#!/usr/bin/env python3
import PyInstaller.__main__
from pathlib import Path

HERE = Path(__file__).parent.absolute()
MAIN = HERE / "__main__.py"


def install():
    pyinstaller_args = ['--name=jodie', '--onefile', str(MAIN)]
    PyInstaller.__main__.run(pyinstaller_args)


if __name__ == "__main__":
    install()
