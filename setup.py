#!/usr/bin/env python
from setuptools import setup

import vers

# PLY compiles the yacc/lex tables to Python at import time (see ccl.py),
# so no build-time extension step is needed here.

classifiers = """\
Development Status :: 5 - Production/Stable
Intended Audience :: Developers
Programming Language :: Python
Programming Language :: Python :: 3
Programming Language :: Python :: 3.9
Programming Language :: Python :: 3.10
Programming Language :: Python :: 3.11
Programming Language :: Python :: 3.12
Programming Language :: Python :: 3.13
Programming Language :: Python :: 3.14
Topic :: Internet :: Z39.50"""

setup (name="PyZ3950",
       version= vers.version,
       author = "Aaron Lav",
       author_email = "asl2@pobox.com",
       license = "X",
       description = 'Z39.50 (ZOOM API), ASN.1, and MARC implementations',
       long_description =
       """Pure Python implementation of ASN.1 and Z39.50 v3,
       with a simple MARC parser thrown in.  See the URL for details.""",
       platforms = ["any"],
       classifiers = list(filter(None, classifiers.split("\n"))),
       url = "http://www.pobox.com/~asl2/software/PyZ3950",
       packages = ["PyZ3950"],
       python_requires = ">=3.9")
