Advanced Usage
===============

.. _button_customization:

Form Button Customization
--------------------------

Button Style
~~~~~~~~~~~~

When you use form related macros, you have a couple ways to style buttons.
Before we start to dive into the solutions, let's review some Fomantic basics:
In Fomantic, you have 17 basic button style and 16 inverted button style,
so you have 16 inverted+basic button style classes:

**Basic:** A basic button is less pronounced

- primary basic
- secondary basic
- positive basic
- negative basic
- red basic
- orange basic
- yellow basic
- olive basic
- green basic
- teal basic
- blue basic
- violet basic
- purple basic
- pink basic
- brown basic
- grey basic
- black basic

**Inverted:** A button can be formatted to appear on dark backgrounds

- inverted
- inverted primary
- inverted secondary
- inverted red
- inverted orange
- inverted yellow
- inverted olive
- inverted green
- inverted teal
- inverted blue
- inverted violet
- inverted purple
- inverted pink
- inverted brown
- inverted grey
- inverted black

**Inverted + basic:** Combine two styles.

- inverted basic
- inverted primary basic
- inverted secondary basic
- inverted red basic
- inverted orange basic
- inverted yellow basic
- inverted olive basic
- inverted green basic
- inverted teal basic
- inverted blue basic
- inverted violet basic
- inverted purple basic
- inverted pink basic
- inverted brown basic
- inverted grey basic
- inverted black basic

You will use these names in Flask-FomanticUI.
First, you configuration variables ``FOMANTIC_BUTTON_STYLE`` to set
a global form button style:

.. code-block:: python

    from flask import Flask
    from flask_fomanticui import FomanticUI

    app = Flask(__name__)
    fomantic = FomanticUI(app)

    app.config['FOMANTIC_BUTTON_STYLE'] = 'inverted black basic'


Or you can use ``button_style`` parameter when using ``render_ui_form``, ``render_ui_field`` and ``render_ui_form_row``, this parameter will overwrite
``FOMANTIC_BUTTON_STYLE``:

.. code-block:: jinja

    {% from 'fomantic/form.html' import render_ui_form %}

    {{ render_ui_form(form, button_style='positive basic') }}

Button Size
~~~~~~~~~~~~

Similarly, you can use this way to control the button size. In Fomantic UI, buttons can have 8 sizes:

- mini
- tiny
- small 
- medium
- large
- big
- huge 
- massive

So, the size names used in Flask-FomanticUI will be:

- mini
- tiny
- small 
- medium
- large
- big
- huge 
- massive

Now you can use a configuration variable called ``FOMANTIC_BUTTON_STYLE`` to set global form button size:

.. code-block:: python

    from flask import Flask
    from flask_fomanticui import FomanticUI

    app = Flask(__name__)
    fomantic = FomanticUI(app)

    app.config['FOMANTIC_BUTTON_SIZE'] = 'small'  # default to ''

there also a parameter called ``button_size`` in form related macros (it will overwrite ``FOMANTIC_BUTTON_SIZE``):

.. code-block:: jinja

    {% from 'fomantic/form.html' import render_ui_form %}

    {{ render_ui_form(form, button_size='big') }}


What if I have three buttons in one form, and I want they have different styles and sizes?
The answer is ``button_map`` parameter in form related macros.
``button_map`` is a dictionary that mapping button field name
to Fomantic button style names. For example, ``{'submit': 'positive basic'}``.
Here is a more complicate example:

.. code-block:: jinja

    {% from 'fomantic/form.html' import render_ui_form %}

    {{ render_ui_form(form, button_map={'submit': 'primary', 'cancel': 'orange', 'delete': 'negative'}) }}

It will overwrite ``button_style`` and ``FOMANTIC_BUTTON_STYLE``.
