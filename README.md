# Flask-FomanticUI (Building)

[![Build status](https://github.com/juniors90/Flask-FomanticUI/actions/workflows/testing-package.yml/badge.svg)](https://github.com/juniors90/Flask-FomanticUI/actions)
[![codecov](https://codecov.io/gh/juniors90/Flask-FomanticUI/branch/main/graph/badge.svg?token=YNCV9C9GIG)](https://codecov.io/gh/juniors90/Flask-FomanticUI)
![docstr-cov](https://img.shields.io/endpoint?url=https://jsonbin.org/juniors90/Flask-FomanticUI/badges/docstr-cov)
[![Forks](https://img.shields.io/github/forks/juniors90/Flask-FomanticUI)](https://github.com/juniors90/Flask-FomanticUI/stargazers)
[![star](https://img.shields.io/github/stars/juniors90/Flask-FomanticUI?color=yellow)](https://github.com/juniors90/Flask-FomanticUI/network/members)
[![issues](https://img.shields.io/github/issues/juniors90/Flask-FomanticUI?color=teal)](https://github.com/juniors90/Flask-FomanticUI/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/Flask-FomanticUI?color=green)](https://github.com/juniors90/Flask-FomanticUI/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)


## Requirements

Python 3.8+

## Dependecies for this project.

- [Flask(>=2.0.2)](https://flask.palletsprojects.com/en/2.0.x/) for build the backend.

## intallation

You can install via pip:

```cmd
    $> pip install Flask-FomanticUI
```
   
For development, clone the [official github repository](https://github.com/juniors90/Flask-FomanticUI) instead and use:

```cmd
    $ git clone git@github.com:juniors90/Flask-FomanticUI.git
    $ cd Flask-FomanticUI
    $ python3 -m venv venv
    $ source venv/bin/activate
    (venv) $ pip install -r requirements/dev.txt
```

## Quick start

```python
    from flask import Flask, render_template_string
    from flask_fomanticui import FomanticUI
    
    app = Flask(__name__)
    fomantic = FomanticUI(app)

    # routes
    @app.route("/")
    def index():
        # Make data:
        return render_template()

    if __name__ == "__main__":
        app.run(port=5000, debug=True)
```

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

