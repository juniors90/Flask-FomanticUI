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


def test_render_ui_field_row(app, client, hello_form):
    @app.route("/form")
    def test():
        form = hello_form()
        return render_template_string(
            """
                {% from 'fomantic/form_ui.html' import render_ui_field_row %}
                {{ render_ui_field_row([form.username, form.password]) }}
                """,
            form=form,
        )

    response = client.get("/form")
    data = response.get_data(as_text=True)
    assert '<div class="two fields">' in data
    assert '<div class="field required">' in data
    assert '<label for="username">Username</label>' in data
    assert '<label for="password">Password</label>' in data
    assert '<input class="" id="username"' in data
    assert '<input class="" id="password"' in data
