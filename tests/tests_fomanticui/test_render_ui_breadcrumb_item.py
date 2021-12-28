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

from flask import render_template_string


def test_render_breadcrumb_item_active(app, client):
    @app.route("/not_active_item")
    def foo():
        return render_template_string(
            """
            {% from 'fomantic/nav.html' import render_ui_breadcrumb_item %}
            {{ render_ui_breadcrumb_item('bar', 'Bar') }}
                """
        )

    @app.route("/active_item")
    def bar():
        return render_template_string(
            """
            {% from 'fomantic/nav.html' import render_ui_breadcrumb_item %}
            {{ render_ui_breadcrumb_item('bar', 'Bar') }}
            """
        )

    response = client.get("/not_active_item")
    data = response.get_data(as_text=True)
    assert '<a class="section" href="/active_item">Bar</a>' in data

    response = client.get("/active_item")
    data = response.get_data(as_text=True)
    assert '<a class="active section">Bar</a>' in data
    assert '<i class="right chevron icon divider"></i>' in data
