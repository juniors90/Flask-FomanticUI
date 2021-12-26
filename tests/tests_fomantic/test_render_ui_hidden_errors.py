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

from flask_wtf import FlaskForm

from wtforms import HiddenField, SubmitField
from wtforms.validators import DataRequired


def test_render_ui_hidden_errors(app, client):
    class TestForm(FlaskForm):
        hide = HiddenField(
            "Hide", validators=[DataRequired("Hide field is empty.")]
        )
        submit = SubmitField()

    @app.route("/error", methods=["GET", "POST"])
    def error():
        form = TestForm()
        if form.validate_on_submit():
            pass
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_field,
                                               render_ui_hidden_errors %}
        <form method="post">
            {{ form.hidden_tag() }}
            {{ render_ui_hidden_errors(form) }}
            {{ render_ui_field(form.submit) }}
        </form>
        """,
            form=form,
        )

    response = client.post("/error", follow_redirects=True)
    data = response.get_data(as_text=True)
    assert "Hide field is empty." in data
