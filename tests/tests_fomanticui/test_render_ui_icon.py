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


def test_render_ui_icon(app, client):
    @app.route("/icon")
    def icon():
        return render_template_string(
            """
        {% from 'fomantic/utils.html' import render_ui_icon %}
            {{ render_ui_icon('user') }}
        """
        )

    @app.route("/icon-color")
    def icon_color():
        return render_template_string(
            """
        {% from 'fomantic/utils.html' import render_ui_icon %}
        {% for c in  ["primary",
                      "secondary",
                      "red",
                      "orange",
                      "yellow",
                      "olive",
                      "green",
                      "teal",
                      "blue",
                      "violet",
                      "purple",
                      "pink",
                      "brown",
                      "grey",
                      "black"] %}
            {{ render_ui_icon('user', color=c) }}
        {% endfor %}
        """
        )

    @app.route("/icon-style-css")
    def icon_style():
        return render_template_string(
            """
        {% from 'fomantic/utils.html' import render_ui_icon %}
        {% for c in ['WhiteSmoke','MintCream','Beige'] %}
            {{ render_ui_icon('user', color=c) }}
        {% endfor %}
        """
        )

    response = client.get("/icon")
    data = response.get_data(as_text=True)
    assert '<i class="user icon"></i>' in data

    response = client.get("/icon-color")
    data = response.get_data(as_text=True)
    for c in [
        "primary",
        "secondary",
        "red",
        "orange",
        "yellow",
        "olive",
        "green",
        "teal",
        "blue",
        "violet",
        "purple",
        "pink",
        "brown",
        "grey",
        "black",
    ]:
        assert f'<i class="user {c} icon"></i>' in data

    response = client.get("/icon-style-css")
    data = response.get_data(as_text=True)
    for c in ["WhiteSmoke", "MintCream", "Beige"]:
        assert f'<i class="user icon" style="color: {c}"></i>' in data
