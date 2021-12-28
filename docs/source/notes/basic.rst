Basic Usage
===========

Installation
------------

Create a project folder and a :file:`venv` folder within:

.. tabs::

   .. group-tab:: macOS/Linux

      .. code-block:: text

         $ mkdir myproject
         $ cd myproject
         $ python3 -m venv venv

   .. group-tab:: Windows

      .. code-block:: text

         > mkdir myproject
         > cd myproject
         > py -3 -m venv venv

.. code-block:: bash

    $ pip install Flask-FomanticUI


Initialization
--------------

.. code-block:: python

    from flask import Flask
    from flask_fomanticui import FomanticUI

    app = Flask(__name__)

    fomantic = FomanticUI(app)


Resources helpers
-----------------

Flask-FomanticUI provides two helper functions to load `Fomantic UI <https://fomantic-ui.com/>`_
resources in the template: ``fomantic.load_css()`` and ``fomantic.load_js()``.

Call it in your base template, for example:

.. code-block:: jinja

    <head>
    ....
    {{ fomantic.load_css() }}
    </head>
    <body>
    ...
    {{ fomantic.load_js() }}
    </body>

You can pass ``version`` to pin the Fomantic UI 2.8.8 version you want to use.
It defaults to load files from CDN. Set ``FOMANTIC_SERVE_LOCAL`` to ``True`` to use built-in local files.
However, these methods are optional, you can also write ``<href></href>`` and ``<script></script>`` tags
to include Fomantic UI resources (from your ``static`` folder or CDN) manually by yourself.

Starter template
----------------

For reasons of flexibility, Flask-FomanticUI doesn't include built-in base templates
(this may change in the future). For now,  you have to create a base template yourself.
Be sure to use an HTML5 doctype and include a viewport meta tag for proper responsive behaviors.
Here's an example base template:

.. code-block:: html

    <!doctype html>
    <html lang="en">
        <head>
            {% block head %}
            <!-- Required meta tags -->
            <meta charset="utf-8">
            <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">

            {% block styles %}
                <!-- Fomantic-UI CSS -->
                {{ fomantic.load_css() }}
            {% endblock %}

            <title>Your page title</title>
            {% endblock %}
        </head>
        <body>
            <!-- Your page content -->
            {% block content %}{% endblock %}

            {% block scripts %}
                <!-- Optional JavaScript -->
                {{ fomantic.load_js() }}
            {% endblock %}
        </body>
    </html>

Use this in your templates folder (suggested names are ``base.html`` or ``layout.html`` etc.),
and inherit it in child templates. See `Template Inheritance <http://flask.pocoo.org/docs/1.0/patterns/templateinheritance/>`_ for
more details on inheritance.

.. _macros_list:

Macros
------

+------------------------------+--------------------------------+--------------------------------------------------------------------+
| Macro                        | Templates Path                 | Description                                                        |
+==============================+================================+====================================================================+
| render_ui_field()            | fomantic/form_ui.html          | Render a WTForms form field.                                       |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_form()             | fomantic/form_ui.html          | Render a WTForms form.                                             |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_form_row()         | fomantic/form_ui.html          | Render a row of a grid form.                                       |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_hidden_errors()    | fomantic/form_ui.html          | Render error messages for hidden form field.                       |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_pager()            | fomantic/pagination.html       | Render a basic Flask-SQLAlchemy pagniantion.                       |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_pagination()       | fomantic/pagination.html       | Render a standard Flask-SQLAlchemy pagination.                     |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_nav_item()         | fomantic/nav.html              | Render a navigation item.                                          |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_breadcrumb_item()  | fomantic/nav.html              | Render a breadcrumb item.                                          |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_static()              | fomantic/utils.html            | Render a resource reference code (i.e. ``<link>``, ``<script>``).  |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_messages()         | fomantic/utils.html            | Render flashed messages send by ``flash()`` function.              |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_icon()             | fomantic/utils.html            | Render a Fomantic icon.                                            |
+------------------------------+--------------------------------+--------------------------------------------------------------------+
| render_ui_table()            | fomantic/table.html            | Render a table with given data.                                    |
+------------------------------+--------------------------------+--------------------------------------------------------------------+

How to use these macros? It's quite simple, just import them from the
corresponding path and call them like any other macro:

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_form %}

    {{ render_ui_form(form) }}

Go to the :doc:`macros` page to see the detailed usage for these macros.

Configurations
--------------

+-----------------------------+---------------+------------------------------------------------------------------------------+
| Configuration Variable      | Default Value | Description                                                                  |
+=============================+===============+==============================================================================+
| FOMANTIC_SERVE_LOCAL        | ``False``     | If set to ``True``, local resources will be used for ``load_*`` methods.     |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_BUTTON_STYLE       | ``'primary'`` | Default form button style, will change to ``primary`` in next major release. |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_BUTTON_SIZE        | ``""``        | Default form button size.                                                    |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_ICON_SIZE          | ``None``      | Default icon size.                                                           |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_ICON_COLOR         | ``None``      | Default icon color, follow the context with ``currentColor`` if not set.     |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_MSG_CATEGORY       | ``None'``     | Default flash message category.                                              |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_TABLE_VIEW_TITLE   | ``'View'``    | Default title for view icon of table actions.                                |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_TABLE_EDIT_TITLE   | ``'Edit'``    | Default title for edit icon of table actions.                                |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_TABLE_DELETE_TITLE | ``'Delete'``  | Default title for delete icon of table actions.                              |
+-----------------------------+---------------+------------------------------------------------------------------------------+
| FOMANTIC_TABLE_NEW_TITLE    | ``'New'``     | Default title for new icon of table actions.                                 |
+-----------------------------+---------------+------------------------------------------------------------------------------+

.. 
    tip:: See :ref:`button_customization` to learn how to customize form buttons.
