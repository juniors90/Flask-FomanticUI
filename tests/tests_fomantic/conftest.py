#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file was part of Flask-Bootstrap and was modified under the terms of
# its BSD License. Copyright (c) 2013, Marc Brinkmann. All rights reserved.
#
# This file was part of Bootstrap-Flask and was modified under the terms of
# its MIT License. Copyright (c) 2018 Grey Li. All rights reserved.
#
# This file is part of the
# Flask-FomanticUI Project (https://github.com/juniors90/Flask-FomanticUI/).
# Copyright (c) 2021, Ferreira Juan David
# License: MIT
# Full Text: https://github.com/juniors90/Flask-FomanticUI/blob/master/LICENSE

# =============================================================================
# TESTS
# =============================================================================

import re

from flask_fomantic import FomanticUI

import pytest as pt


@pt.fixture(autouse=True)
def fomantic(app):
    yield FomanticUI(app)


@pt.fixture
def cdn_suiv():
    fomantic_version = re.search(
        r"(\d+\.\d+\.\d+)", str(FomanticUI.fomantic_version)
    ).group(1)
    return "Fomantic UI - " + fomantic_version


@pt.fixture
def cdn_jqv():
    jquery_version = re.search(
        r"(\d+\.\d+\.\d+)", str(FomanticUI.jquery_version)
    ).group(1)
    return "jQuery v" + jquery_version


@pt.fixture
def local_suiv():
    fomantic_version = re.search(
        r"(\d+\.\d+\.\d+)", str(FomanticUI.fomantic_version)
    ).group(1)
    return "Fomantic UI - " + fomantic_version


@pt.fixture
def local_jsv():
    js_version = re.search(
        r"(\d+\.\d+\.\d+)", str(FomanticUI.fomantic_version)
    ).group(1)
    return "Fomantic UI - " + js_version


@pt.fixture
def local_jqv():
    jq_version = re.search(
        r"(\d+\.\d+\.\d+)", str(FomanticUI.jquery_version)
    ).group(1)
    return "jQuery v" + jq_version
