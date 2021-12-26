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

from flask_fomantic import (
    link_css_with_sri,
    scripts_with_sri,
    simple_link_css,
    simple_scripts_js,
)


def test_link_css():
    css_html_sri = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.css" integrity="sha256-ckBg2pN9ZF9KPn+vY00JXAkdqE1nv20iGM2haZhCBl4=" crossorigin="anonymous">'  # noqa: E501
    css_sri = "sha256-ckBg2pN9ZF9KPn+vY00JXAkdqE1nv20iGM2haZhCBl4="
    css_url = (
        "https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.css"
    )
    css = (
        '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm'
        + '/fomantic-ui@2.8.8/dist/semantic.min.css">'
    )
    assert css == simple_link_css(css_url)
    assert css_sri in link_css_with_sri(css_url, css_sri)
    assert css_url in link_css_with_sri(css_url, css_sri)
    assert css_html_sri == link_css_with_sri(css_url, css_sri)


def test_simple_link_css_js():
    js_html_sri = '<script src="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.js" integrity="sha256-VxL9ZXOItJ0i4nJLm39HIoX8u3cCRPRkDjMSXZ/RiQQ=" crossorigin="anonymous"></script>'  # noqa: E501
    js_sri = "sha256-VxL9ZXOItJ0i4nJLm39HIoX8u3cCRPRkDjMSXZ/RiQQ="
    js_url = (
        "https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.js"
    )
    js = (
        '<script src="https://cdn.jsdelivr.net/'
        + 'npm/fomantic-ui@2.8.8/dist/semantic.min.js"></script>'
    )
    assert js == simple_scripts_js(js_url)
    assert js_sri in scripts_with_sri(js_url, js_sri)
    assert js_url in scripts_with_sri(js_url, js_sri)
    assert js_html_sri == scripts_with_sri(js_url, js_sri)


def test_fomantic_find_local_resource(app, fomantic):
    with app.app_context(), app.test_request_context():
        app.config["FOMANTIC_SERVE_LOCAL"] = True
        app.config["SERVER_NAME"] = "localhost"
        url_css = fomantic.load_css()
        url_js_and_jquery = fomantic.load_js()
    css = (
        '<link rel="stylesheet" type="text/css" '
        + 'href="/static/css/semantic.min.css">'
    )
    js = '<script src="/static/js/semantic/semantic.min.js"></script>'
    jquery = '<script src="/static/js/semantic/jquery.min.js"></script>'
    assert css in url_css
    assert js in url_js_and_jquery
    assert jquery in url_js_and_jquery


def test_fomantic_find_cdn_resource(app, fomantic):
    with app.app_context(), app.test_request_context():
        app.config["FOMANTIC_SERVE_LOCAL"] = False
        url_css = fomantic.load_css()
        url_js_and_jquery = fomantic.load_js()
    css = '<link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.css" integrity="sha256-ckBg2pN9ZF9KPn+vY00JXAkdqE1nv20iGM2haZhCBl4=" crossorigin="anonymous">'  # noqa: E501
    js = '<script src="https://cdn.jsdelivr.net/npm/fomantic-ui@2.8.8/dist/semantic.min.js" integrity="sha256-VxL9ZXOItJ0i4nJLm39HIoX8u3cCRPRkDjMSXZ/RiQQ=" crossorigin="anonymous"></script>'  # noqa: E501
    jquery = '<script src="https://cdn.jsdelivr.net/npm/jquery@3.3.1/dist/jquery.min.js" integrity="sha256-FgpCb/KJQlLNfOu91ta32o/NMZxltwRo8QtmkMRdAu8=" crossorigin="anonymous"></script>'  # noqa: E501
    assert css in url_css
    assert js in url_js_and_jquery
    assert jquery in url_js_and_jquery
