# web_server

The web server backend for the covite project.

## Content

- [Developers](#developers)
  - [web_server uses Poetry](#web-server-uses-poetry)
  - [web_server uses heroku to deploy](#web-server-uses-heroku-to-deploy)
  - [web_server uses types (with pyright)](#web-server-uses-types--with-pyright-)
  - [Getting started with Poetry](#getting-started-with-poetry)

## Developers

### web_server uses Poetry

1. Install the python package manager [Poetry](https://github.com/python-poetry/poetry) (also see [the full instructions in the doc](https://python-poetry.org/docs/#installation)). On Linux and OSX, use:

```bash
curl -sSL https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python
```

2. Install the dependencies. Make sure you're at the root of this repository and run the following command:

```bash
poetry install
```

This will install all the dependencies listed in `pyproject.toml`, respecting the version specified in `poetry.lock`.

### web_server uses Python 3.8.2

On windows, `choco install python` installs the last released python. On linux, Python 3.8.2 can be installed using pyenv.

#### On linux, how to install pyenv

See [pyenv wiki](https://github.com/pyenv/pyenv/wiki) and [pyenv installer](https://github.com/pyenv/pyenv-installer#install)

```
sudo apt-get update; sudo apt-get install --no-install-recommends make build-essential libssl-dev zlib1g-dev libbz2-dev libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev xz-utils tk-dev libxml2-dev libxmlsec1-dev libffi-dev liblzma-dev && curl https://pyenv.run | bash
```

You can then run `pyenv install 3.8.2`. Use `pyenv versions` and `pyenv version`
to know what python version pyenv shims.

### web_server uses heroku to deploy

Install the heroku cli:

`https://devcenter.heroku.com/articles/heroku-cli#other-installation-methods`

### web_server uses types (with pyright)

If you use VSCode, you can install pyright's extension. Note that because of how
young pyright is, it's hard to get things working nicely with `# pyright: strict` enabled. You can ignore errors with one of:

- `cast(Any, <expression>)`, with `from typings import Any, cast`
- `<line> # type: ignore`

### web_server uses editorconfig

Install the corresponding extension for your IDE.

### Getting started with Poetry

Poetry is quite similar to yarn and npm:

- To add a package to the project use `poetry add ...`
- Use `poetry add --dev ...` for a developer dependency (example: `selenium`)
- To run any CLI installed in the project use `poetry run ...`
  - To run `django-admin` use `poetry run django-admin`
  - To run python with the project dependencies available, use `poetry run python ...`. This applies both to running python files, and starting a python shell.
  - To run `manage.py`, use `poetry run python manage.py`
  - ALTERNATIVELY, you can use `poetry shell` to activate the virtual environment, and then freely run the CLIs installed in it: `django-admin ...`, `python manage.py ...`, etc.
