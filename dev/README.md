# Dev Info

## Getting Started

### Dependencies

#### Runtimes and Utilities

- Python - 3.6
- VirtualEnv - 15.1.0

#### Packages

- Django - 1.11
- Pytz - 2017.3

### Pip & Python VirtualEnv

To create a virtual environment for development:

`virtualenv --prompt=geek-text --python=python3 .venv`

and then to activate the venv:

`source .venv/bin/activate`

To install the Python dependencies for this project, run:

`pip install -r requirements.txt`

### Running Project

The following requires that a virtual environment be created and set up for
the project. To do so, refer to the
[Pip & Python VirualEnv](#pip--python-virtualenv) instructions in this repo.

The get the current state of the project running for development work, the
following must be done:

1. Activate the venv for this repo
2. Apply any migrations needed by the database
3. Run the test server

These steps can be done as follows:

```bash
source .venv/bin/activate && cd webapp
python manage.py migrate
python manage.py runserver
```

By this point, you should have a test server up and running to start making
changes and iterating on your implementation.

### Running Specs

[To-Do]

## Repo Layout

### Django Apps

These are the apps under the `webapp` directory at the root of the repo. These
represent the major features denoted for the app, with the `geek_text` app
being the main app that coordinates common functionality and resources as well
as integrations amongst the various other apps.

[To-Do]

### Dev Directory

#### README.md

That's this doc right here, all info about working on and with this project
should be found right here. There should be ample detail so that the
instructions are as lenient for beginners as possible.

Brief details on any scripts and directories in the `dev` directory should be
listed here, with the scripts or directories haivng their own internal comments
or READMEs.

#### specs.pdf

This document contains the original specs denoted for this team project and
contains information on all the various details about needed features and some
misc info on non-technical project requirements.

### Deployment

This directory contains any scripts, templates, and generally any files that
are used to deploy this project.

[To-Do]

