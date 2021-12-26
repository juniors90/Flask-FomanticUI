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


from flask import current_app

from flask_fomantic import cdn_base

import pytest as pt


@pt.mark.usefixtures("client")
class TestFomanticUI:
    def test_extension_init(self, app):
        with app.app_context():
            extensions = current_app.extensions
        assert "fomantic" in extensions
        assert "fomantic_ui" not in extensions

    def test_load_css_with_default_versions(self, fomantic):
        rv = fomantic.load_css()
        cdn = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.css" integrity="sha256-ckBg2pN9ZF9KPn+vY00JXAkdqE1nv20iGM2haZhCBl4=" crossorigin="anonymous">'  # noqa:E501
        fomantic_css = (
            '<link rel="stylesheet" href="'
            + cdn_base
            + "/fomantic-ui@"
            + fomantic.fomantic_version
            + "/dist/"
            + fomantic.fomantic_css_filename
            + '" integrity="'
            + fomantic.fomantic_css_integrity
            + '" crossorigin="anonymous">'
        )
        assert fomantic_css == rv
        assert fomantic_css == cdn
        assert rv == cdn


def test_fomantic_get_sri(app, fomantic):
    with app.app_context():
        app.config["FOMANTIC_SERVE_LOCAL"] = True
        assert (
            fomantic._get_sri(
                name="fomantic_js",
                version="2.8.8",
                sri="sha256-CgSoWC9w5wNmI1aN8dIMK+6DPelUEtvDr+Bc2m/0Nx8=",
            )
            == "sha256-CgSoWC9w5wNmI1aN8dIMK+6DPelUEtvDr+Bc2m/0Nx8="
        )
        assert (
            fomantic._get_sri(name="fomantic_js", version="2.8.8", sri=None)
            is None
        )
