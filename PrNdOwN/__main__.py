#!/usr/bin/env python
# Date 31/08/2021
# Author ybenel
from __future__ import unicode_literals

import sys

if __package__ is None and not hasattr(sys, "frozen"):
    # direct call of __main__.py
    import os.path
    PATH = os.path.realpath(os.path.abspath(__file__))
    sys.path.append(os.path.dirname(os.path.dirname(PATH)))

import PrNdOwN


if __name__ == '__main__':
    PrNdOwN.main()
