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

from flask import flash, render_template_string


def test_render_ui_messages(app, client):
    @app.route("/messages")
    def test_messages():
        flash("test message", "danger")
        return render_template_string(
            """{% from 'fomantic/utils.html' import render_ui_messages %}
               {{ render_ui_messages() }}"""
        )

    @app.route("/container")
    def test_container():
        flash("test message", "danger")
        return render_template_string(
            """{% from 'fomantic/utils.html' import render_ui_messages %}
               {{ render_ui_messages(container=True) }}"""
        )

    @app.route("/dismissible")
    def test_dismissible():
        flash("test message", "danger")
        return render_template_string(
            """{% from 'fomantic/utils.html' import render_ui_messages %}
               {{ render_ui_messages(dismissible=True) }}"""
        )

    @app.route("/category")
    def test_category():
        flash("A simple default alert—check it out!")
        for category in [
            "dark",
            "danger",
            "debug",
            "light",
            "critical",
            "error",
            "info",
            "warning",
            "success",
            "secondary",
            "primary",
        ]:
            flash(f"A simple {category} alert—check it out!", category)
        return render_template_string(
            """{% from 'fomantic/utils.html' import render_ui_messages %}
               {{ render_ui_messages(dismissible=True) }}"""
        )

    response = client.get("/messages")
    data = response.get_data(as_text=True)
    assert '<div class="ui error message">' in data

    response = client.get("/container")
    data = response.get_data(as_text=True)
    assert '<div class="ui text container">' in data

    response = client.get("/dismissible")
    data = response.get_data(as_text=True)
    assert '<i class="close icon"></i>' in data
    assert '<ul class="list">' not in data
    assert "test message" in data

    response = client.get("/category")
    data = response.get_data(as_text=True)
    for cat in ["floating", "black", "error"]:
        assert f'<div class="ui {cat} message">' in data
