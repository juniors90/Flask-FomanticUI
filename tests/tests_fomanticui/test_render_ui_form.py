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

from flask import current_app, render_template_string

from flask_wtf import FlaskForm

from wtforms import (
    BooleanField,
    FileField,
    MultipleFileField,
    PasswordField,
    RadioField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired


def test_render_ui_form(app, client, example_form):
    @app.route("/form")
    def test():
        form = example_form()
        return render_template_string(
            """
                {% from "fomantic/form_ui.html" import render_ui_form %}
                {{ render_ui_form(form,
                                  form_title='Title for Shipping Information',
                                  inverted=true,
                                  form_type='inline',
                                  button_map={'submit_button': 'primary'})}}
                """,
            form=form,
        )

    response = client.get("/form")
    data = response.get_data(as_text=True)
    assert '<input class="" id="name"' in data
    assert '<input class="" id="username"' in data
    assert '<input class="" id="country_code"' in data
    assert '<input id="radio_field-0" name="radio_field"' in data
    assert '<input class=" ui primary button " id="submit_button"' in data
    assert 'class="ui form error inverted inline" role="form">' in data
    assert (
        '<label for="radio_field" style="color: #FFFFFF;">'
        + "This is a radio field</label>"
        in data
    )


# test WTForm field description for TextFieldField
def test_form_description_for_textfield(app, client):
    class TestForm(FlaskForm):
        field1 = StringField("First Field", description="This is field one.")
        submit_button = SubmitField("Submit Form")

    @app.route("/description")
    def description():
        form = TestForm()
        return render_template_string(
            """
                    {% from "fomantic/form_ui.html" import render_ui_form %}
                    {{ render_ui_form(form,
                                form_title='Title for Shipping Information',
                                button_map={'submit_button': 'primary'}) }}
                    """,
            form=form,
        )

    response = client.get("/description")
    data = response.get_data(as_text=True)
    assert "Title for Shipping Information" in data
    assert (
        '<small style="margin-left:0.1in; font-size: small;">'
        + "This is field one.</small>"
        in data
    )
    assert (
        '<input class="" id="field1" name="field1" type="text" value="">'
        in data
    )


# test WTForm fields for render_ui_form and render_field
def test_render_ui_form_enctype(app, client):
    class SingleUploadForm(FlaskForm):
        sample = FileField("Sample upload")
        submit_button = SubmitField("Submit Form")

    class MultiUploadForm(FlaskForm):
        photos = MultipleFileField("Multiple photos")
        submit_button = SubmitField("Submit Form")

    @app.route("/single")
    def single():
        form = SingleUploadForm()
        return render_template_string(
            """
            {% from "fomantic/form_ui.html" import render_ui_form %}
            {{ render_ui_form(form,
                                form_title='Title for Shipping Information',
                                button_map={'submit_button': 'primary'}) }}
        """,
            form=form,
        )

    @app.route("/multi")
    def multi():
        form = MultiUploadForm()
        return render_template_string(
            """
            {% from "fomantic/form_ui.html" import render_ui_form %}
            {{ render_ui_form(form,
                                form_title='Title for Shipping Information',
                                button_map={'submit_button': 'primary'}) }}
        """,
            form=form,
        )

    response = client.get("/single")
    data = response.get_data(as_text=True)
    assert "multipart/form-data" in data

    response = client.get("/multi")
    data = response.get_data(as_text=True)
    assert "multipart/form-data" in data


# test render_kw class for WTForms field
def test_form_render_kw_class(app, client):
    class LoginForm(FlaskForm):
        username = StringField("Username")
        phone = PasswordField(
            "Password", render_kw={"class": "my-password-class"}
        )
        submit_button = SubmitField(
            "Submit Form", render_kw={"class": "my-awesome-class"}
        )

    @app.route("/render_kw")
    def render_kw():
        form = LoginForm()
        return render_template_string(
            """
            {% from "fomantic/form_ui.html" import render_ui_form %}
            {% for c in ['my-custom-class',
                         'inverted primary basic',
                         'inverted secondary basic']%}
                {{ render_ui_form(form,
                                  form_title='Title for Shipping Information',
                                  button_map={'submit_button': c }) }}
            {% endfor %}
            """,
            form=form,
        )

    response = client.get("/render_kw")
    data = response.get_data(as_text=True)
    assert "my-awesome-class" in data
    assert "button" in data
    assert 'class="my-password-class"' in data
    assert "class-not-found" not in data
    assert 'class=" ui my-custom-class button my-awesome-class"' in data
    assert 'class=" ui inverted primary basic button my-awesome-class"' in data
    assert (
        'class=" ui inverted secondary basic button my-awesome-class"' in data
    )


def test_button_size(app, client, hello_form):
    with app.app_context():
        assert current_app.config["FOMANTIC_BUTTON_SIZE"] == ""
    app.config["FOMANTIC_BUTTON_SIZE"] = "medium"
    assert "fomantic" in app.extensions

    @app.route("/form")
    def test():
        form = hello_form()
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form) }}
        """,
            form=form,
        )

    response = client.get("/form")
    data = response.get_data(as_text=True)
    assert "medium" in data

    @app.route("/form2")
    def test_overwrite():
        form = hello_form()
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form, button_size='large') }}
        """,
            form=form,
        )

    response = client.get("/form2")
    data = response.get_data(as_text=True)
    assert "medium" not in data
    assert "large" in data


def test_button_style(app, client, hello_form):
    with app.app_context():
        assert current_app.config["FOMANTIC_BUTTON_STYLE"] == "primary"
    app.config["FOMANTIC_BUTTON_STYLE"] = "secondary"

    @app.route("/form")
    def test():
        form = hello_form()
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form) }}
        """,
            form=form,
        )

    response = client.get("/form")
    data = response.get_data(as_text=True)
    assert "secondary" in data

    @app.route("/form2")
    def test_overwrite():
        form = hello_form()
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form, button_style='success') }}
        """,
            form=form,
        )

    response = client.get("/form2")
    data = response.get_data(as_text=True)
    assert "primary" not in data
    assert "success" in data

    @app.route("/form3")
    def test_button_map():
        form = hello_form()
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form, button_map={'submit': 'negative'}) }}
        """,
            form=form,
        )

    response = client.get("/form3")
    data = response.get_data(as_text=True)
    assert "primary" not in data
    assert "negative" in data


def test_error_message_for_radiofield_and_booleanfield(app, client):
    class TestForm(FlaskForm):
        remember = BooleanField("Remember me", validators=[DataRequired()])
        option = RadioField(
            choices=[
                ("dog", "Dog"),
                ("cat", "Cat"),
                ("bird", "Bird"),
                ("alien", "Alien"),
            ],
            validators=[DataRequired()],
        )

    @app.route("/error", methods=["GET", "POST"])
    def error():
        form = TestForm()
        if form.validate_on_submit():
            pass
        return render_template_string(
            """
        {% from 'fomantic/form_ui.html' import render_ui_form %}
        {{ render_ui_form(form) }}
        """,
            form=form,
        )

    response = client.post("/error", follow_redirects=True)
    data = response.get_data(as_text=True)
    assert "This field is required" in data
