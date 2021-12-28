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


def test_render_render_ui_nav_item_active(app, client):
    @app.route("/active")
    def foo():
        return render_template_string(
            """
                {% from 'fomantic/nav.html' import render_ui_nav_item %}
                {{ render_ui_nav_item('foo', 'Foo') }}
                """
        )

    response = client.get("/active")
    data = response.get_data(as_text=True)
    assert ' <a class="active item"' in data

    @app.route("/not_active")
    def bar():
        return render_template_string(
            """{% from 'fomantic/nav.html' import render_ui_nav_item %}
               {{ render_ui_nav_item('foo', 'Foo') }}"""
        )

    response = client.get("/not_active")
    data = response.get_data(as_text=True)
    assert '<a class="item"' in data

    @app.route("/color")
    def color():
        return render_template_string(
            """
            {% from 'fomantic/nav.html' import render_ui_nav_item %}
            {{ render_ui_nav_item('color',
                                  'Color',
                                  iname='envelope',
                                  color='teal') }}
            """
        )

    response = client.get("/color")
    data = response.get_data(as_text=True)
    assert '<a class="active teal item" href="/color">' in data
    assert '<i class="envelope icon"></i>Color</a>' in data
