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

# =====================================================================
# TESTS
# =====================================================================


def test_can_import_package():
    import flask_fomantic  # noqa


def test_can_initialize_app_and_extesion():
    from flask import Flask
    from flask_fomantic import FomanticUI

    app = Flask(__name__)
    FomanticUI(app)


def test_can_initialize_app_and_extesion_with_factory_func():
    from flask import Flask
    from flask_fomantic import FomanticUI

    app = Flask(__name__)
    fomantic = FomanticUI()
    fomantic.init_app(app)
