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
# DOCS
# =============================================================================

"""Flask-FomanticUI.

Implementation of FomanticUI in Flask.
"""

# =============================================================================
# META
# =============================================================================

from .core import _FomanticUI


class FomanticUI(_FomanticUI):
    """Base class for palies the FomanticUI framework.

    Initilize the extension::

        from flask import Flask
        from flask_fomantic import FomanticUI

        app = Flask(__name__)
        fomantic = FomanticUI(app)


    Or with the application factory::


        from flask import Flask
        from flask_fomantic import FomanticUI

        Fomantic = FomanticUI()

        def create_app():
            app = Flask(__name__)
            fomantic.init_app(app)

    """

    jquery_version = "3.3.1"
    fomantic_version = "2.8.8"
    fomantic_css_integrity = (
        "sha256-ckBg2pN9ZF9KPn+vY00JXAkdqE1nv20iGM2haZhCBl4="
    )
    fomantic_js_integrity = (
        "sha256-VxL9ZXOItJ0i4nJLm39HIoX8u3cCRPRkDjMSXZ/RiQQ="
    )
    jquery_integrity = "sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8="
    static_folder = "fomantic"
