#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""PrNdOwN setup file.

Examples:
    Windows::

        python setup.py py2exe

    Linux::

        python setup.py install

    Build source distribution::

        python setup.py sdist

    Build platform distribution::

        python setup.py bdist

    Build the translations::

        python setup.py build_trans

    Build with updates disabled::

        python setup.py build --no-updates

Requirements:

    * GNU gettext utilities

Notes:
    If you get 'TypeError: decoding Unicode is not supported' when you run
    py2exe then apply the following patch::

        http://sourceforge.net/p/py2exe/patches/28/

    Basic steps of the setup::

        * Run pre-build tasks
        * Call setup handler based on OS & options
            * Set up hicolor icons (if supported by platform)
            * Set up fallback pixmaps icon (if supported by platform)
            * Set up package level pixmaps icons (*.png)
            * Set up package level i18n files (*.mo)
            * Set up scripts (executables) (if supported by platform)
        * Run setup

"""

from distutils import cmd, log
from distutils.core import setup
from distutils.command.build import build

import os
import sys
import glob
from shutil import copyfile
from subprocess import call

PY2EXE = len(sys.argv) >= 2 and sys.argv[1] == "py2exe"

if PY2EXE:
    try:
        import py2exe
    except ImportError as error:
        print(error)
        sys.exit(1)

from PrNdOwN import (
    __author__,
    __appname__,
    __contact__,
    __version__,
    __license__,
    __projecturl__,
    __description__,
    __packagename__,
    __descriptionfull__
)

# Setup can not handle unicode
__packagename__ = str(__packagename__)


def on_windows():
    """Returns True if OS is Windows."""
    return os.name == "nt"


class BuildBin(cmd.Command):

    description = "build the PrNdOwN binary file"
    user_options = []

    def initialize_options(self):
        self.scripts_dir = None

    def finalize_options(self):
        self.scripts_dir = os.path.join("build", "_scripts")

    def run(self):
        if not os.path.exists(self.scripts_dir):
            os.makedirs(self.scripts_dir)

        copyfile(os.path.join(__packagename__, "__main__.py"),
                 os.path.join(self.scripts_dir, "PrNdOwN"))

class Build(build):

    """Overwrite the default 'build' behaviour."""

    sub_commands = [
        ("build_bin", None)] + build.sub_commands

    def run(self):
        build.run(self)


# Overwrite cmds
cmdclass = {
    "build": Build,
    "build_bin": BuildBin
}


def linux_setup():
    scripts = []
    package_data = {}
    # Add pixmaps icons (*.png) & i18n files
    package_data[__packagename__] = [
        "ascii/*"
    ]
    # Add scripts
    scripts.append("build/_scripts/PrNdOwN")

    setup_params = {
        "scripts": scripts,
        "package_data": package_data
    }

    return setup_params


def windows_setup():
    def normal_setup():
        package_data = {}

        # Add pixmaps icons (*.png) & i18n files
        package_data[__packagename__] = [
        "ascii/*"
        ]

        setup_params = {
            "package_data": package_data
        }

        return setup_params

    def py2exe_setup():
        windows = []

        # py2exe dependencies & options
        # TODO change directory for ffmpeg.exe & ffprobe.exe
        dependencies = [
            "C:\\Windows\\System32\\ffmpeg.exe",
            "C:\\Windows\\System32\\ffprobe.exe",
            "C:\\python27\\DLLs\\MSVCP90.dll"
        ]
        #############################################


        # We have to manually add the translation files since py2exe cant do it
        for lang in os.listdir("PrNdOwN\\ascii"):
            dst = os.path.join("ascii", lang)
            src = os.path.join("ascii", dst)

        # Add GUI executable details
        windows.append({
            "script": "build\\_scripts\\PrNdOwN"
        })

        setup_params = {
            "windows": windows,
            "options": {"py2exe": options}
        }

        return setup_params

    if PY2EXE:
        return py2exe_setup()

    return normal_setup()


if on_windows():
    params = windows_setup()
else:
    params = linux_setup()

setup(
    author              = __author__,
    name                = __appname__,
    version             = __version__,
    license             = __license__,
    author_email        = __contact__,
    url                 = __projecturl__,
    description         = __description__,
    long_description    = __descriptionfull__,
    packages            = [__packagename__],
    cmdclass            = cmdclass,

    **params
)
