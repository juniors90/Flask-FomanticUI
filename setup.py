#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file is part of the
#   Flask-FomanticUI Project (https://github.com/juniors90/Flask-FomanticUI/).
# Copyright (c) 2022, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-FomanticUI/blob/master/LICENSE

# =====================================================================
# DOCS
# =====================================================================

"""This file is for distribute and install Flask-FomanticUI"""

# ======================================================================
# IMPORTS
# ======================================================================

import os
import pathlib

from setuptools import setup  # noqa

# =============================================================================
# CONSTANTS
# =============================================================================

PATH = pathlib.Path(os.path.abspath(os.path.dirname(__file__)))


REQUIREMENTS = ["Flask>=2.0.2"]

with open(PATH / "flask_fomanticui" / "__init__.py") as fp:
    for line in fp.readlines():
        if line.startswith("__version__ = "):
            VERSION = line.split("=", 1)[-1].replace('"', "").strip()
            break


with open("README.md") as fp:
    LONG_DESCRIPTION = fp.read()


# =============================================================================
# FUNCTIONS
# =============================================================================

setup(
    name="Flask-FomanticUI",
    version=VERSION,
    description="Flask extension to allow easy embedding of Fomantic-UI CSS Framework.",  # noqa: E501
    long_description=LONG_DESCRIPTION,
    long_description_content_type="text/markdown",
    author="Ferreira Juan David",
    author_email="juandavid9a0@gmail.com",
    url="https://github.com/juniors90/Flask-FomanticUI",
    packages=["flask_fomanticui"],
    include_package_data=True,
    platforms="any",
    license="The MIT License",
    install_requires=REQUIREMENTS,
    keywords=["Fomantic-UI", "Flask", "Framework CSS"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3.8",
        "Topic :: Internet :: WWW/HTTP :: Dynamic Content",
        "Topic :: Software Development :: Libraries :: Python Modules",
    ],
)
