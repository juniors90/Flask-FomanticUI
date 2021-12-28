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


def test_render_pager(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003

    @app.route("/pager")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(100):
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/pagination.html' import render_ui_pager %}
            {{ render_ui_pager(pagination) }}
            """,
            pagination=pagination,
            messages=messages,
        )

    @app.route("/pager-inverted-color")
    def test_inverted():
        db.drop_all()
        db.create_all()
        for i in range(100):
            msg = Message()
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/pagination.html' import render_ui_pager %}
            {{ render_ui_pager(pagination,
                               extra_classes='inverted',
                               color_active_item='teal') }}
            """,
            pagination=pagination,
            messages=messages,
        )

    response = client.get("/pager")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination menu">' in data
    assert "Prev" in data
    assert "Next" in data
    assert '<div class="disabled item">' in data
    assert '<a class="active item" href="/pager?page=2">' in data

    response = client.get("/pager?page=2")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination menu">' in data
    assert "Prev" in data
    assert "Next" in data
    assert '<div class="disabled item">' in data
    assert '<a class="active item" href="/pager?page=1">' in data

    response = client.get("/pager-inverted-color")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert "Prev" in data
    assert "Next" in data
    assert '<div class="disabled item">...</div>' in data
    assert (
        '<a class="active teal item" href="/pager-inverted-color?page=2">'
        in data
    )

    response = client.get("/pager-inverted-color?page=2")
    data = response.get_data(as_text=True)
    assert '<nav aria-label="Page navigation">' in data
    assert '<div class="ui pagination inverted menu">' in data
    assert "Prev" in data
    assert "Next" in data
    assert '<div class="disabled item">...</div>' in data
    assert (
        '<a class="active teal item" href="/pager-inverted-color?page=1">'
        in data
    )
