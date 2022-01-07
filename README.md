# Flask-FomanticUI

[![Build status](https://github.com/juniors90/Flask-FomanticUI/actions/workflows/testing-package.yml/badge.svg)](https://github.com/juniors90/Flask-FomanticUI/actions)
[![codecov](https://codecov.io/gh/juniors90/Flask-FomanticUI/branch/main/graph/badge.svg?token=YNCV9C9GIG)](https://codecov.io/gh/juniors90/Flask-FomanticUI)
![docstr-cov](https://img.shields.io/endpoint?url=https://jsonbin.org/juniors90/Flask-FomanticUI/badges/docstr-cov)
[![Documentation Status](https://readthedocs.org/projects/flask-fomanticui/badge/?version=latest)](https://flask-fomanticui.readthedocs.io/en/latest/?badge=latest)
[![Forks](https://img.shields.io/github/forks/juniors90/Flask-FomanticUI)](https://github.com/juniors90/Flask-FomanticUI/stargazers)
[![star](https://img.shields.io/github/stars/juniors90/Flask-FomanticUI?color=yellow)](https://github.com/juniors90/Flask-FomanticUI/network/members)
[![issues](https://img.shields.io/github/issues/juniors90/Flask-FomanticUI?color=teal)](https://github.com/juniors90/Flask-FomanticUI/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/Flask-FomanticUI?color=green)](https://github.com/juniors90/Flask-FomanticUI/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)

Flask-FomanticUI is a collection of Jinja macros for [Fomantic UI](https://fomantic-ui.com/) and
[Flask](https://flask.palletsprojects.com/en/2.0.x/) for the global style. Very similar
to [Bootstrap-Flask](https://github.com/greyli/bootstrap-flask). 

## Features

- [x] Table generation: Render data objects (dict or class objects) to Fomantic UI Table.
- [x] Paginate generation: Render Flask-SQLAlchemy `Pagination` object to Fomantic UI Pagination.
- [x] Form generation: Render Flask-WTF/WTForms form object to Fomantic UI Form, etc.


## Requirements

Python 3.8+

## Dependecies for this project.

- [Flask(>=2.0.2)](https://flask.palletsprojects.com/en/2.0.x/) for build the backend.

## intallation

You can install via pip:

```cmd
    $> pip install Flask-FomanticUI
```

## Example

Register the extension:

```python
from flask import Flask
# To follow the naming rule of Flask extension, although
# this project's name is Flask-FomanticUI, the actual package
# installed is named `flask_fomanticui`.
from flask_fomanticui import FomanticUI

app = Flask(__name__)
fomantic = FomanticUI(app)
```

Assuming you have a Flask-WTF form like this:

```python
class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), Length(8, 150)])
    submit = SubmitField()
    remember = BooleanField('Remember me')
```

Now with the `render_form` macro:

```html
{% from 'fomanticui/form_ui.html' import render_ui_form %}
<html>
<head>
<!-- Fomantic UI - CSS -->
</head>
<body>

<h2>Login</h2>
{{ render_ui_form(form) }}

<!-- Fomantic UI - JS -->
</body>
</html>
```

You will get a form like this with only one line code (i.e. `{{ render_ui_form(form) }}`):

![form rendering](https://raw.githubusercontent.com/juniors90/Flask-FomanticUI/master/docs/source/_static/form-example.PNG)

When the validation fails, the error messages will be rendered with proper style:

![error form rendering](https://raw.githubusercontent.com/juniors90/Flask-FomanticUI/master/docs/source/_static/error-form-example.PNG)

Read the [Basic Usage](https://flask-fomanticui.readthedocs.io/en/latest/notes/basic.html) 
docs for more details.

## Links

- [Documentation](https://flask-fomanticui.readthedocs.io)
- [Example Application](https://github.com/juniors90/Flask-FomanticUI/tree/main/sample_app)
- [PyPI Releases](https://pypi.org/project/Flask-FomanticUI/)
- [Changelog](https://github.com/juniors90/Flask-FomanticUI/blob/main/CHANGELOG.rst)


## Authors

- Ferreira, Juan David

Please submit bug reports, suggestions for improvements and patches via
the (E-mail: juandavid9a0@gmail.com).

## Contributors

Credits goes to these peoples:

<a href="https://github.com/juniors90/Flask-FomanticUI/graphs/contributors">
  <img src="https://contrib.rocks/image?repo=juniors90/Flask-FomanticUI" />
</a>

## Official repository and Issues

- https://github.com/juniors90/Flask-FomanticUI


## License

`Flask-FomanticUI` is free software you can redistribute it and/or modify it
under the terms of the MIT License. For more information, you can see the
[LICENSE](https://github.com/juniors90/Flask-FomanticUI/blob/main/LICENSE) file
for details.