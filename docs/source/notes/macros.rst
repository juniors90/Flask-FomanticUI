Use Macros
==========

These macros will help you to generate Fomantic-markup codes quickly and easily.

render_ui_nav_item()
--------------------

Render a Fomantic nav item.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/nav.html' import render_ui_nav_item %}

    <div class="ui attached stackable menu">
        {{ render_ui_nav_item('index', 'Home', 'home', 'teal') }}
        {{ render_ui_nav_item('explore', 'Explore', 'envelope', 'red') }}
        {{ render_ui_nav_item('about', 'About', 'map', 'purple') }}
    </div>

API
~~~~

.. py:function:: render_ui_nav_item(endpoint, text, iname, color=None, **kwargs)

    :param endpoint: The endpoint used to generate ``URL``.
    :param text: The text that will displayed on the item.
    :param iname: The icon name.
    :param color: Default: ``None``.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.


render_ui_breadcrumb_item()
----------------------------

Render a Fomantic UI breadcrumb item.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/nav.html' import render_ui_breadcrumb_item %}

    <nav class="ui breadcrumb">
        {{ render_ui_breadcrumb_item('home', 'Home') }}
        {{ render_ui_breadcrumb_item('users', 'Users') }}
        {{ render_ui_breadcrumb_item('posts', 'Posts') }}
        {{ render_ui_breadcrumb_item('comments', 'Comments') }}
    </nav>

API
~~~~

.. py:function:: render_ui_breadcrumb_item(endpoint, text, icon='right chevron', **kwargs)

    :param endpoint: The endpoint used to generate ``URL``.
    :param text: The text that will displayed on the item.
    :param icon: Te icon name. Default: ``right chevron``.
    :param kwargs: Additional keyword arguments pass to ``url_for()``.

render_ui_field()
-----------------

Render a form input for form field created by
`Flask-WTF/WTForms <https://wtforms.readthedocs.io/en/master/fields/>`_.

Example
~~~~~~~~
.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_field %}

    <form class="ui form error" method="post">
        {{ form.csrf_token() }}
        {{ render_ui_field(form.username) }}
        {{ render_ui_field(form.password) }}
        {{ render_ui_field(form.submit) }}
    </form>

You can pass extra keyword arguements like ``class`` or ``placeholder`` for each HTML element.

Notice that a ``placeholder`` is only allowed by `W3C validation <https://validator.w3.org/>`_
when the input type is ``email``, ``number``, ``password``, ``search``, ``tel``,
``text`` or ``url``. However, it is possible to use a placeholder for input types
such as ``datetime``.

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_field %}

    <form class="ui form error" method="post">
        {{ form.csrf_token() }}
        {{ render_ui_field(form.username, class='myClass') }}
        {{ render_ui_field(form.password, placeholder='Your Password') }}
        {{ render_ui_field(form.submit) }}
    </form>

Notice the ``class`` value here will overwrite the ``render_kw={'class': '...'}`` you defined in
the form class. Flask-FomanticUI will combine the class value you passed with the ``class`` key of
the ``render_kw`` dict or the ``class`` keyword argments with Fomantic classes.


API
~~~~

.. py:function:: render_ui_field(field,\
                                 form_type="basic",\
                                 inverted=None,\
                                 horizontal_columns=('sixteen', 'sixteen', 'sixteen'),\
                                 button_style="",\
                                 button_size="",\
                                 button_map={})

    :param field: The form field (attribute) to render.
    :param form_type: Can be ``inline``. See the
                     Fomantic docs for details on different form layouts.
    :param inverted: If ``True``, define a `inverted <https://fomantic-ui.com/collections/form.html#inverted>`_
                     form class. Default to ``None``.
    :param horizontal_columns: *TODO in new relases:* (When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``(column-wide-mobile,
                              column-wide-tablet, column-wide-computer)``).
    :param button_style: Set button style for ``SubmitField``.
                         Accept `Fomantic UI button style <https://fomantic-ui.com/elements/button.html>`_
                         name (i.e. primary, secondary, positive, negative, etc.). Default to ``primary`` (e.g.
                         ``ui primary``). This will overwrite config ``FOMANTIC_BUTTON_STYLE``.
    :param button_size: Set button size for ``SubmitField``. Accept Fomantic UI button.
                        size name: ``mini``, ``tiny``, ``small``, ``medium``, ``large``, ``big``, ``huge``, ``massive``.
                        Default to ``""`` and this will overwrite config ``FOMANTIC_BUTTON_SIZE``.
    :param button_map: It given by ``button_map.get(field.name, button_style)``. See :ref:`button_customization` to
                       learn how to customize form buttons.

.. tip::
    
    See :ref:`button_customization` to learn how to customize form buttons.

render_ui_form()
----------------

Render a complete form element for form object created by Flask-WTF/WTForms.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_form %}

    {{ render_ui_form(form) }}

API
~~~~

.. py:function:: render_ui_form(form,\
                                action="",\
                                method="post",\
                                inverted=None,\
                                extra_classes=None,\
                                role="form",\
                                form_type="basic",\
                                horizontal_columns=('sixteen', 'sixteen', 'sixteen'),\
                                enctype=None,\
                                button_map={},\
                                button_style="",\
                                button_size="",\
                                id="",\
                                novalidate=False,\
                                render_kw={},\
                                form_title=None)

    :param form: The form to output.
    :param action: The URL to receive form data.
    :param method: ``<form>`` method attribute.
    :param inverted: If ``True``, define a `inverted <https://fomantic-ui.com/collections/form.html#inverted>`_
                     form class. Default to ``None``.
    :param extra_classes: The classes to add to the ``<form>``.
    :param role: ``<form>`` role attribute.
    :param form_type: One of ``inline``. See the
                     Fomantic docs for details on different form layouts.
    :param horizontal_columns: When using the horizontal layout, layout forms
                              like this. Must be a 3-tuple of ``('sixteen', 'sixteen', 'sixteen')``.
    :param enctype: ``<form>`` enctype attribute. If ``None``, will
                    automatically be set to ``multipart/form-data`` if a
                    :class:`~wtforms.fields.FileField` or :class:`~wtforms.fields.MultipleFileField` is present in the form.
    :param button_map: A dictionary, mapping button field name to `Fomantic UI button style <https://fomantic-ui.com/elements/button.html>`_
                       names. For example, ``{'submit': 'positive'}``. This will overwrite ``button_style`` and ``FOMANTIC_BUTTON_STYLE``.
    :param button_style: Set button style for ``SubmitField``. Accept Fomantic UI button style name (i.e. primary, 
                         secondary, positive, negative, etc.), default to ``primary`` (e.g. ``ui primary``). This will
                         overwrite config ``FOMANTIC_BUTTON_STYLE``.
    :param button_size: Set button size for ``SubmitField``. Accept `Fomantic button size <https://fomantic-ui.com/elements/button.html#size>`_ 
                        name: mini, tiny, small, medium, large, big, huge, massive. Default to ``""`` and this will overwrite config ``FOMANTIC_BUTTON_SIZE``.
    :param id: The ``<form>`` id attribute.
    :param novalidate: Flag that decide whether add ``novalidate`` attribute in ``<form>``.
    :param render_kw: A dictionary, specifying custom attributes for the ``<form>``.
    :param form_title: The title for the form.

.. tip::
    
    See :ref:`button_customization` to learn how to customize form buttons.


render_ui_hidden_errors()
-------------------------

Render error messages for hidden form field (``wtforms.HiddenField``).

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_field,
                                           render_ui_hidden_errors %}

    <form class="ui form error" method="post">
        {{ form.hidden_tag() }}
        {{ render_ui_field(form.username) }}
        {{ render_ui_field(form.password) }}
        {{ render_ui_field(form.submit) }}
        {{ render_ui_hidden_errors(form) }}
    </form>

API
~~~~

.. py:function:: render_ui_hidden_errors(form)

    :param form: Form whose errors should be rendered.


render_ui_field_row()
---------------------

Render a row of a grid form with the given fields.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_field_row %}

    <form class="ui form error" method="post">
        {{ form.csrf_token }}
        {{ render_ui_field_row([form.username, form.password]) }}
        {{ render_ui_field(form.submit) }}
        {{ render_ui_field(form.remember) }}
    </form>

is equivalent to

.. code-block:: jinja

    {% from 'fomantic/form_ui.html' import render_ui_field %}

    <form class="ui form" method="post">
        {{ form.csrf_token() }}
        <div class="two fields">
            {{ render_ui_field(form.username) }}
            {{ render_ui_field(form.password) }}
        </div>
        {{ render_ui_field(form.submit) }}
        {{ render_ui_field(form.remember) }}
    </form>

API
~~~~

.. py:function:: render_ui_field_row(fields,\
                                     row_class={"number":[\
                                        "one",\
                                        "two",\
                                        "three",\
                                        "four",\
                                        "five",\
                                        "six",\
                                        "seven",\
                                        "eight",\
                                        "nine",\
                                        "ten"\
                                        ]\
                                    })

    :param fields: An iterable of fields to render in a row.
    :param row_class: A dictionary, mapping the number of fields to a class definition that should be applied to
                      the div column that contains the fields number. For example: ``<div class="two fields">...</div>``.


render_ui_pager()
-----------------

Render a simple pager for query pagination object created by Flask-SQLAlchemy.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/pagination.html' import render_ui_pager %}

    {{ render_ui_pager(pagination) }}

API
~~~~

.. py:function:: render_ui_pager(pagination,\
                                       fragment='',\
                                       prev='left chevron',\
                                       next='right chevron',\
                                       extra_classes=None,\
                                       color_active_item=None,\
                                        **kwargs)

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param fragment: Add URL fragment into link, such as ``#comment``.
    :param prev: Icon to use for the "previous page" button. Default: ``'left chevron'``.
    :param next: Icon to use for the "next page" button.  Default: ``'right chevron'``.
    :param extra_classes: The classes to add to the pagination menu. Can be ``'inverted'``. Default to ``None``.
    :param color_active_item: Can be ``"red"``, ``"orange"``, ``"yellow"``, ``"olive"``,
                              ``"green"``, ``"teal"``, ``"blue"``, ``"violet"``, ``"purple"``,
                              ``"pink"``, ``"brown"``, ``"grey"``, ``"black"``.
                              Default: ``None``.
    :param kwargs: Additional arguments passed to ``url_for``.


render_ui_pagination()
----------------------

Render a standard pagination for query pagination object created by Flask-SQLAlchemy.

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/pagination.html' import render_ui_pagination %}

    {{ render_ui_pagination(pagination) }}

API
~~~~

.. py:function:: render_ui_pagination(pagination,\
                                        endpoint=None,\
                                        prev='left chevron',\
                                        next='right chevron',\
                                        ellipses='…',\
                                        args={},\
                                        fragment='',\
                                        extra_classes=None,\
                                        color_active_item=None)

    :param pagination: :class:`~flask_sqlalchemy.Pagination` instance.
    :param endpoint: Which endpoint to call when a page number is clicked.
                    :func:`~flask.url_for` will be called with the given
                    endpoint and a single parameter, ``page``. If ``None``,
                    uses the requests current endpoint.
    :param prev: Icon to use for the "previous page" button. If
                ``None``, the button will be hidden.
    :param next: Icon to use for the "next page" button. If
                ``None``, the button will be hidden.
    :param ellipses: Symbol/text to use to indicate that pages have been
                    skipped. If ``None``, no indicator will be printed.
    :param args: Additional arguments passed to :func:`~flask.url_for`. If
                ``endpoint`` is ``None``, uses :attr:`~flask.Request.args` and
                :attr:`~flask.Request.view_args`
    :param fragment: Add URL fragment into link, such as ``#comment``.
    :param extra_classes: The classes to add to the pagination menu. Can be ``'inverted'``. Default to ``None``.
    :param color_active_item: The color classes to add to the pagination item. Default to ``None``.


render_static()
----------------
Render a resource reference code (i.e. ``<link>``, ``<script>``).

Example
~~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/utils.html' import render_static %}

    {{ render_static('css', 'style.css') }}

API
~~~~

.. py:function:: render_static(type, filename_or_url, local=True)

    :param type: Resources type, one of ``css``, ``js``, ``icon``.
    :param filename_or_url: The name of the file, or the full URL when ``local`` set to ``False``.
    :param local: Load local resources or from the passed ``URL``.


render_ui_messages()
--------------------

Render Fomantic alerts for flash messages send by ``flask.flash()``.

Example
~~~~~~~~

Flash the message in your view function with ``flash(message, category)``:

.. code-block:: python

    from flask import flash

    @app.route('/test')
    def test():
        flash('a info message', 'info')
        flash('a danger message', 'danger')
        return your_template

Render the messages in your base template (normally below the navbar):

.. code-block:: jinja

    {% from 'fomantic/utils.html' import render_ui_messages %}

    <nav>...</nav>
    {{ render_ui_messages() }}
    <main>...</main>


API
~~~~

.. py:function:: render_ui_messages(messages=None, \
                                   title=None, \
                                   container=True, \
                                   transform={...}, \
                                   default_category=config.FOMANTIC_MSG_CATEGORY, \
                                   dismissible=False)

    :param messages: The messages to show. If not given, default to get from ``flask.get_flashed_messages(with_categories=True)``.
    :param title: If true, will enable dismiss animate when click the dismiss button.
    :param container: If true, will output a complete ``<div class="ui container">`` element, otherwise just the messages each wrapped in a ``<div>``.
    :param transform: A dictionary of mappings for categories. Will be looked up case-insensitively. Default maps all Python loglevel names to Fomantic CSS classes.
    :param default_category: If a category does not has a mapping in transform, it is passed through unchanged. ``default_category`` will be used when ``category`` is empty.
    :param dismissible: If true, will output a button to close an alert. For fully functioning dismissible alerts, you must use the alerts JavaScript plugin.
    

When you call ``flash('message', 'category')``, there are 8 category options available, mapping to Fomantic UI alerts type:

- dark,
- danger,
- debug,
- light,
- critical,
- error,
- info,
- warning,
- success

If you want to use HTML in your message body, just wrapper your message string with ``flask.Markup`` to tell Jinja it's safe:

.. code-block:: python

    from flask import flash, Markup

    @app.route('/test')
    def test():
        flash(Markup('a info message with a link: <a href="/">Click me!</a>'), 'info')
        return your_template


render_ui_table()
-----------------

Render a Fomantic table with given data.

Example
~~~~~~~

.. code-block:: python

    @app.route('/test')
    def test():
        data = Message.query.all()
        return render_template('test.html', data=data)

.. code-block:: jinja

    {% from 'fomantic/table.html' import render_ui_table %}

    {{ render_ui_table(data) }}

API
~~~~

.. py:function:: render_ui_table(data,\
                              titles=None,\
                              primary_key='id',\
                              primary_key_title='#',\
                              caption=None,\
                              caption_class=None,\
                              caption_icon=None,\
                              table_classes=None,\
                              header_classes=None,\
                              responsive=False,\
                              responsive_class='table-responsive',\
                              show_actions=False,\
                              actions_title='Actions',\
                              model=None,\                              
                              custom_actions=None,\
                              view_url=None,\
                              edit_url=None,\
                              delete_url=None,\
                              new_url=None)
                      
    :param data: An iterable of data objects to render. Can be dicts or class objects.
    :param titles: An iterable of tuples of the format (prop, label) e.g ``[('id', '#')]``, if not provided,
                will automatically detect on provided data, currently only support SQLAlchemy object.
    :param primary_key: Primary key identifier for a single row, default to ``id``.
    :param primary_key_title: Primary key title for a single row, default to ``#``.
    :param caption: A caption to attach to the table.
    :param caption_class: A caption class to attach to the table. Default to ``None``.
    :param caption_icon: A caption icon to attach to the table. Default to ``None``.
    :param table_classes: A string of classes to apply to the table (e.g ``'selectable inverted'``).
    :param header_classes: A string of classes to apply to the table header (e.g ``'full-width'``).
    :param responsive: Whether to enable/disable table responsiveness.
    :param responsive_class: The responsive class to apply to the table. Default to ``'table-responsive'``.
    :param stackable_class: A string of classes such that specify how it stacks table content responsively
                            using ``stackable`` or ``stackable`` class. Default to ``None``,
    :param show_actions: Whether to display the actions column. Default is ``False``.
    :param model: The model used to build custom_action, view, edit, delete URLs.
    :param actions_title: Title for the actions column header. Default is ``'Actions'``.
    :param custom_actions: A list of tuples for creating custom action buttons, where each tuple contains
                ('Title Text displayed on hover', 'fomantic icon name', 'URL tuple or fixed URL string')
                (e.g. ``[('Run', 'play-fill', ('run_report', [('report_id', ':id')]))]``).
    :param view_url: URL string or URL tuple in ``('endpoint', [('url_parameter_name', ':db_model_fieldname')])``
                to use for the view action.
    :param edit_url: URL string or URL tuple in ``('endpoint', [('url_parameter_name', ':db_model_fieldname')])``
                to use for the edit action.
    :param delete_url: URL string or URL tuple in ``('endpoint', [('url_parameter_name', ':db_model_fieldname')])``
                to use for the delete action.
    :param new_url: URL string to use for the create action.

To set the URLs for table actions, you will need to pass either a fixed URL string or
an URL tuple in the form of ``('endpoint', [('url_parameter_name', ':db_model_fieldname')])``:

- ``endpoint``: endpoint of the view, normally the name of the view function
- ``[('url_parameter_name', ':db_model_fieldname')]``: a list of two-element tuples, the tuple should contain the
  URL parameter name and the corresponding field name in the database model (starts with a ``:`` mark to indicate
  it's a variable, otherwise it will becomes a fixed value). ``db_model_fieldname`` may also contain dots to access
  relationships and their fields (e.g. ``user.name``).

Remember to set the ``model`` when setting this URLs, so that Flask-FomanticUI will know where to get the actual value
when building the ``URL``.

For example, for the view below:

.. code-block:: python

    class Message(Model):
        id = Column(primary_key=True)

    @app.route('/messages/<int:message_id>')
    def view_message(message_id):
        pass

To pass the URL point to this view for ``view_url``, the value
will be: ``view_url=('view_message', [('message_id', ':id')])``.
Here is the full example:

.. code-block:: python

    @app.route('/test')
    def test():
        data = Message.query.all()
        return render_template('test.html', data=data, Message=Message)

.. code-block:: jinja

    {% from 'fomantic/table.html' import render_ui_table %}

    {{ render_ui_table(data, model=Message, view_url=('view_message', [('message_id', ':id')])) }}

The following arguments are expect to accpet an URL tuple:

- ``custom_actions``
- ``view_url``
- ``edit_url``
- ``delete_url``

When setting the ``delete_url``, you will also need to enable the
CSRFProtect extension provided by Flask-WTF, so that
the CSRF protection can be added to the delete button:

.. code-block:: text

    $ pip install flask-wtf

.. code-block:: python

    from flask_wtf import CSRFProtect

    csrf = CSRFProtect(app)

By default, it will enable the CSRF token check for all the POST requests, read more about this extension in its
`documentation <https://flask-wtf.readthedocs.io/en/latest/csrf/>`_.


render_ui_icon()
----------------

Render a Fomantic UI icon.

Example
~~~~~~~

.. code-block:: jinja

    {% from 'fomantic/utils.html' import render_ui_icon %}

    {{ render_ui_icon('heart', 'teal') }}

API
~~~~

.. py:function:: render_ui_icon(type=None, color=config.FOMANTIC_ICON_COLOR)

    :param type: The name of icon, you can find all available names at Fomantic Icon.
    :param color: The color of icon, follow the context with ``currentColor`` if not set.
                  Accept values are Fomantic style name (one of ``primary``, ``secondary``,
                  ``red``, ``orange``, ``yellow``, ``olive``, ``green``, ``teal``, ``blue``,
                  ``violet``, ``purple``, ``pink``, ``brown``, ``grey``, ``black``) or any
                  valid color string (e.g. ``'red'``, ``'#ddd'`` or ``'rgb(250,250,250)'``),
                  default to use configuration ``FOMANTIC_ICON_COLOR`` (default value is ``None``).
