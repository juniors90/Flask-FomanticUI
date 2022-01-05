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

"""Flask-FomanticUI.

Implementation of Fomantic UI in Flask.
"""

# =============================================================================
# IMPORTS
# =============================================================================


import warnings

from flask import Blueprint, Markup, current_app, url_for

try:  # pragma: no cover
    from wtforms.fields import HiddenField
except ImportError:  # pragma: no cover
    # docstr-coverage:excused `no one is reading this anyways`
    def is_hidden_field_filter(field):
        raise RuntimeError("WTForms is not installed.")

else:
    # docstr-coverage:excused `no one is reading this anyways`
    def is_hidden_field_filter(field):
        return isinstance(field, HiddenField)


cdn_base = "https://cdn.jsdelivr.net/npm"


# docstr-coverage:excused `no one is reading this anyways`
def raise_helper(message):  # pragma: no cover
    raise RuntimeError(message)


def get_table_titles(data, primary_key, primary_key_title):
    """Detect and build the table titles tuple from ORM object.

    .. note::
        Currently only support SQLAlchemy.
    """
    if not data:
        return []
    titles = []
    for k in data[0].__table__.columns.keys():
        if not k.startswith("_"):
            titles.append((k, k.replace("_", " ").title()))
    titles[0] = (primary_key, primary_key_title)
    return titles


# docstr-coverage:excused `no one is reading this anyways`
def link_css_with_sri(url, sri):
    return f'<link rel="stylesheet" href="{url}" integrity="{sri}" crossorigin="anonymous">'  # noqa: E501


# docstr-coverage:excused `no one is reading this anyways`
def simple_link_css(url):
    return f'<link rel="stylesheet" href="{url}">'


# docstr-coverage:excused `no one is reading this anyways`
def scripts_with_sri(url, sri):
    return f'<script src="{url}" integrity="{sri}" crossorigin="anonymous"></script>'  # noqa: E501


# docstr-coverage:excused `no one is reading this anyways`
def simple_scripts_js(url):
    return f'<script src="{url}"></script>'


class _FomanticUI(object):
    """Base extension class for different Fomantic UI versions.

    .. versionadded:: 0.0.1
    """

    fomantic_version = None
    jquery_version = None
    fomantic_css_integrity = None
    fomantic_js_integrity = None
    jquery_integrity = None
    static_folder = None
    fomantic_css_filename = "semantic.min.css"
    fomantic_js_filename = "semantic.min.js"
    jquery_filename = "jquery.min.js"

    def __init__(self, app=None):
        if app is not None:
            self.init_app(app)

    def init_app(self, app):
        """Application factory."""

        # default settings
        app.config.setdefault("FOMANTIC_SERVE_LOCAL", False)
        app.config.setdefault("FOMANTIC_BUTTON_STYLE", "primary")
        app.config.setdefault("FOMANTIC_BUTTON_SIZE", "")
        app.config.setdefault("FOMANTIC_ICON_COLOR", None)
        app.config.setdefault("FOMANTIC_ICON_SIZE", None)
        app.config.setdefault("FOMANTIC_ERROR_HEADER", "Action Forbidden")  # noqa: E501
        app.config.setdefault("FOMANTIC_CHECKBOX_HEADER_ERROR", "Action Forbidden")  # noqa: E501
        app.config.setdefault("FOMANTIC_RADIO_HEADER_ERROR", "Action Forbidden")  # noqa: E501
        app.config.setdefault(
            "FOMANTIC_MSG_CATEGORY", None
        )  # change primary by None
        app.config.setdefault("FOMANTIC_TABLE_VIEW_TITLE", "View")
        app.config.setdefault("FOMANTIC_TABLE_EDIT_TITLE", "Edit")
        app.config.setdefault("FOMANTIC_TABLE_DELETE_TITLE", "Delete")
        app.config.setdefault("FOMANTIC_TABLE_NEW_TITLE", "New")
        if not hasattr(app, "extensions"):  # pragma: no cover
            app.extensions = {}
        app.extensions["fomantic"] = self
        blueprint = Blueprint(
            "fomantic",
            __name__,
            static_folder=f"static/{self.static_folder}",
            static_url_path=f"{app.static_url_path}",
            template_folder="templates",
        )

        app.register_blueprint(blueprint)

        app.jinja_env.globals["fomantic"] = self
        app.jinja_env.globals[
            "fomantic_is_hidden_field"
        ] = is_hidden_field_filter
        app.jinja_env.globals["get_table_titles"] = get_table_titles
        app.jinja_env.globals["warn"] = warnings.warn
        app.jinja_env.globals["raise"] = raise_helper
        app.jinja_env.add_extension("jinja2.ext.do")

    def load_css(self, s_version=None, fomantic_sri=None):
        """Load Fomantic's css resources with given version.

        Parameters
        ----------
        s_version : str
            The version of Fomantic UI.
        fomantic_sri : str
            Subresource Integrity.
        Return
        ------
        scripts_cdn : markupsafe.Markup
            Fomantic UI CDN File.
        """

        serve_local = current_app.config["FOMANTIC_SERVE_LOCAL"]
        s_version = self.fomantic_version if s_version is None else s_version
        fomantic_sri = self._get_sri("fomantic_css", s_version, fomantic_sri)

        if serve_local:
            base_path = "css"
            url = url_for(
                "fomantic.static",
                filename=f"{base_path}/{self.fomantic_css_filename}",
            )
        else:
            base_path = cdn_base + f"/fomantic-ui@{s_version}/dist/"
            url = base_path + self.fomantic_css_filename

        if fomantic_sri:
            css = link_css_with_sri(url, fomantic_sri)
        else:
            css = f'<link rel="stylesheet" type="text/css" href="{url}">'
        scripts_cdn = Markup(css)
        return scripts_cdn

    def _get_js_script(self, version, name, sri):
        """Get <script> tag for JavaScipt resources."""
        serve_local = current_app.config["FOMANTIC_SERVE_LOCAL"]
        paths = {
            "fomantic-ui": f"{self.fomantic_js_filename}",
            "jquery": f"{self.jquery_filename}",
        }

        if serve_local:
            path = "js/semantic"
            url = url_for("fomantic.static", filename=f"{path}/{paths[name]}")
        else:
            url = cdn_base + f"/{name}@{version}/dist/{paths[name]}"

        if sri:
            script_html = scripts_with_sri(url, sri)
        else:
            script_html = simple_scripts_js(url)
        return script_html

    def _get_sri(self, name, version, sri):
        serve_local = current_app.config["FOMANTIC_SERVE_LOCAL"]

        sris = {
            "fomantic_css": self.fomantic_css_integrity,
            "fomantic_js": self.fomantic_js_integrity,
            "jquery": self.jquery_integrity,
        }

        versions = {
            "fomantic_css": self.fomantic_version,
            "fomantic_js": self.fomantic_version,
            "jquery": self.jquery_version,
        }

        if sri is not None:
            return sri
        if version == versions[name] and serve_local is False:
            return sris[name]
        return None

    def load_js(
        self,
        version=None,
        jq_version=None,  # noqa: C901
        fomantic_sri=None,
        jquery_sri=None,
    ):
        """Load Fomantic UI and other resources with given version.

        Parameter
        ---------
        version : str
            The version of Fomantic UI.
        jq_version : str
            The version of jQuery (for Fomantic UI).
        fomantic_sri : str
            Subresource Integrity for Fomantic UI..
        jquery_sri : str
            Subresource Integrity for jQuery.
        Return
        ------
        scripts_cdn : markupsafe.Markup
            Fomantic UI CDN File.
        """

        fui_version = self.fomantic_version if version is None else version
        fui_sri = self._get_sri("fomantic_js", fui_version, fomantic_sri)
        fui_js = self._get_js_script(fui_version, "fomantic-ui", fui_sri)
        jq_version = self.jquery_version if jq_version is None else jq_version
        jquery_sri = self._get_sri("jquery", jq_version, jquery_sri)
        jquery = self._get_js_script(jq_version, "jquery", jquery_sri)
        scripts_cdn = Markup(
            f"""{jquery}
                {fui_js}"""
        )
        return scripts_cdn
