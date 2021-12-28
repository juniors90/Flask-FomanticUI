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

from flask import render_template_string, request

from flask_sqlalchemy import SQLAlchemy


def test_render_ui_pagination(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003

    @app.route("/pagination")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(100):  # noqa: F841
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/pagination.html' import render_ui_pagination %}
            {{ render_ui_pagination(pagination) }}
            """,
            pagination=pagination,
            messages=messages,
        )

    response = client.get("/pagination")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<a class="active item" href="#">1</a>' in data
    assert "10</a>" in data

    response = client.get("/pagination?page=2")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert "1</a>" in data
    assert '<a class="active item" href="#">2</a>' in data
    assert "10</a>" in data


def test_render_ui_pagination_extra_class(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003

    @app.route("/pagination")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(100):  # noqa: F841
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/pagination.html' import render_ui_pagination %}
            {{ render_ui_pagination(pagination, extra_classes="inverted") }}
            """,
            pagination=pagination,
            messages=messages,
        )

    response = client.get("/pagination")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert '<a class="active item" href="#">1</a>' in data
    assert "10</a>" in data

    response = client.get("/pagination?page=2")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert "1</a>" in data
    assert '<a class="active item" href="#">2</a>' in data
    assert "10</a>" in data


def test_render_ui_pagination_extra_class_and_color_item(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003

    @app.route("/pagination")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(100):  # noqa: F841
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/pagination.html' import render_ui_pagination %}
            {{ render_ui_pagination(pagination,
                                    extra_classes="inverted",
                                    color_active_item="teal") }}
            """,
            pagination=pagination,
            messages=messages,
        )

    response = client.get("/pagination")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert '<a class="active teal item" href="#">1</a>' in data
    assert "10</a>" in data

    response = client.get("/pagination?page=2")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert "1</a>" in data
    assert '<a class="active teal item" href="#">2</a>' in data
    assert "10</a>" in data
