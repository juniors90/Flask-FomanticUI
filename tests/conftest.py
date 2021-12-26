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

import typing as t

import flask
from flask import render_template_string

from flask_wtf import FlaskForm

import pytest as pt

from wtforms import (
    BooleanField,
    HiddenField,
    IntegerField,
    PasswordField,
    RadioField,
    StringField,
    SubmitField,
)
from wtforms.validators import DataRequired, Length


class ExampleForm(FlaskForm):
    name = StringField("Name")
    username = StringField(
        "Username", validators=[DataRequired(), Length(1, 20)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(8, 150)]
    )
    country_code = IntegerField("Country Code", validators=[DataRequired()])
    radio_field = RadioField(
        "This is a radio field",
        choices=[
            ("head_radio", "Head radio"),
            ("radio_76fm", "Radio '76 FM"),
            ("lips_106", "Lips 106"),
            ("wctr", "WCTR"),
        ],
    )
    hidden = HiddenField()
    remember = BooleanField("Remember me")
    submit_button = SubmitField("Submit Form")


class HelloForm(FlaskForm):
    name = StringField("Name")
    username = StringField(
        "Username", validators=[DataRequired(), Length(1, 20)]
    )
    password = PasswordField(
        "Password", validators=[DataRequired(), Length(8, 150)]
    )
    remember = BooleanField("Remember me")
    hidden = HiddenField()
    submit = SubmitField()


if t.TYPE_CHECKING:
    from flask.testing import FlaskClient


@pt.fixture
def hello_form():
    return HelloForm


@pt.fixture
def example_form():
    return ExampleForm


@pt.fixture(autouse=True)
def app() -> "flask.Flask":
    app = flask.Flask(__name__)
    app.testing = True
    app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
    app.secret_key = "for test"
    app.debug = False

    @app.route("/")
    def index():
        return render_template_string(
            "{{ semantic.load_css() }}{{ semantic.load_js() }}"
        )

    yield app


@pt.fixture
def client(app: "flask.Flask") -> "FlaskClient":
    context = app.test_request_context()
    context.push()

    with app.test_client() as client:
        yield client

    context.pop()
