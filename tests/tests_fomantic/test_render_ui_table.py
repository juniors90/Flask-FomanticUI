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

from flask_wtf import CSRFProtect


def test_render_simple_table(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003
        text = db.Column(db.Text)

    @app.route("/table")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(10):
            m = Message(text=f"Test message {i+1}")
            db.session.add(m)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        titles = [("id", "#"), ("text", "Message")]
        return render_template_string(
            """
                        {% from 'fomantic/table.html' import render_ui_table %}
                        {{ render_ui_table(messages, titles) }}
                        """,
            titles=titles,
            messages=messages,
        )

    response = client.get("/table")
    data = response.get_data(as_text=True)
    assert '<table class="ui celled table">' in data
    assert "<th>#</th>" in data
    assert "<th>Message</th>" in data
    assert '<td data-label="#">1</td>' in data
    assert "<td>Test message 1</td>" in data


def test_render_customized_table(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003
        text = db.Column(db.Text)

    @app.route("/table")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(10):
            msg = Message(text=f"Test message {i+1}")
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        titles = [("id", "#"), ("text", "Message")]
        return render_template_string(
            """
                {% from 'fomantic/table.html' import render_ui_table %}
                {{ render_ui_table(messages, titles,
                            table_classes='ui selectable inverted table',
                            header_classes='my class',
                            caption='Messages',
                            caption_icon='circular user',
                            caption_class='ui center aligned icon header') }}
                            """,
            titles=titles,
            messages=messages,
        )

    response = client.get("/table")
    data = response.get_data(as_text=True)
    assert '<table class=""ui selectable inverted table"">' not in data
    assert '<thead class="my class">' in data
    assert "<caption>Messages</caption>" not in data
    assert '<div class="ui center aligned icon header">' in data
    assert '<i class="circular user icon"></i>' in data


def test_build_table_titles(app, client):
    db = SQLAlchemy(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003
        text = db.Column(db.Text)

    @app.route("/table")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(10):
            msg = Message(text=f"Test message {i+1}")
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
                    {% from 'fomantic/table.html' import render_ui_table %}
                    {{ render_ui_table(messages) }}
                                """,
            messages=messages,
        )

    response = client.get("/table")
    data = response.get_data(as_text=True)
    assert '<table class="ui celled table">' in data
    assert "<th>#</th>" in data
    assert "<th>Text</th>" in data
    assert '<td data-label="#">1</td>' in data
    assert "<td>Test message 1</td>" in data


def test_build_table_titles_with_empty_data(app, client):
    @app.route("/table")
    def test():
        messages = []
        return render_template_string(
            """
                    {% from 'fomantic/table.html' import render_ui_table %}
                    {{ render_ui_table(messages) }}
                        """,
            messages=messages,
        )

    response = client.get("/table")
    assert response.status_code == 200


def test_customize_icon_title_of_table_actions(app, client):

    app.config["FOMANTIC_TABLE_VIEW_TITLE"] = "Read"
    app.config["FOMANTIC_TABLE_EDIT_TITLE"] = "Update"
    app.config["FOMANTIC_TABLE_DELETE_TITLE"] = "Remove"
    app.config["FOMANTIC_TABLE_NEW_TITLE"] = "Create"

    db = SQLAlchemy(app)
    CSRFProtect(app)

    class Message(db.Model):
        id = db.Column(db.Integer, primary_key=True)  # noqa: A003
        text = db.Column(db.Text)

    @app.route("/table")
    def test():
        db.drop_all()
        db.create_all()
        for i in range(10):
            msg = Message(text=f"Test message {i+1}")
            db.session.add(msg)
        db.session.commit()
        page = request.args.get("page", 1, type=int)
        pagination = Message.query.paginate(page, per_page=10)
        messages = pagination.items
        return render_template_string(
            """
            {% from 'fomantic/table.html' import render_ui_table %}
            {{ render_ui_table(messages, model=model, show_actions=True,
            view_url='/view',
            edit_url='/edit',
            delete_url='/delete',
            new_url='/new') }}
            """,
            model=Message,
            messages=messages,
        )

    response = client.get("/table")
    data = response.get_data(as_text=True)
    assert 'title="Read">' in data
    assert 'title="Update">' in data
    assert 'title="Remove">' in data
    assert 'title="Create">' in data
