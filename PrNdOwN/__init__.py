#!/usr/bin/python
# Updated In 00/04/2020
# Created By ybenel
from __future__ import unicode_literals
import sys
import gettext
import os.path
from .downloader import download
from .colors import get_colors
from .version import __version__
from .info import (
    __author__,
    __appname__,
    __contact__,
    __license__,
    __projecturl__,
    __licensefull__,
    __description__,
    __descriptionfull__,
)
__packagename__ = "PrNdOwN"

gettext.install(__packagename__)
def main():
    try:
        download.runner()
    except KeyboardInterrupt as ky:
        print(get_colors.yellow()+get_colors.red() + "\n[!] CTRL+C Detected \n"+get_colors.cyan()+"Thanks For Usage :)"+get_colors.white())
if __name__ == "__main__":
    main()
