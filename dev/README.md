# Dev Info

## Getting Started

### Dependencies

#### Runtimes and Utilities

- Python - 3.6
- VirtualEnv - 15.1.0

#### Main Packages

- pylint - 1.8.2
- Django - 1.11
- django-seed - 0.1.8
- django-filter - 1.1.0
- boto3 - 1.6.3
- Pillow - 5.0.0

### Pip & Python VirtualEnv

To create a virtual environment for development:

`virtualenv --prompt=geek-text --python=python3 .venv`

and then to activate the venv:

`source .venv/bin/activate`

To install the Python dependencies for this project, run:

`pip install -r requirements.txt`

### AWS Access

To host static and media files, an AWS bucket have been set up for use.
Credentials have been generated for memebers and the pipeline to push
files, the following environment variables are involved in this
configuration:

| Variable | Description |
| --- | --- |
| `DJANGO_BACKEND` | Which storage to use -- `amazon` or `local` |
| `AWS_ACCESS_ID` | ID of AWS user account |
| `AWS_SECRET_ACCESS_KEY` | Secret key for AWS account |
| `AWS_S3_BUCKET` | Name of bucket to use -- `geek-text-resources` |

The values to use for these variables can be obtained by asking Dan.

It is recommended to create a script to `source` that exports all these
variables. This can be done with a script like the following:

```bash
export DJANGO_BACKEND=amazon

export AWS_ACCESS_ID={access-key-here}
export AWS_SECRET_KEY={secret-key-here}

export AWS_S3_BUCKET=geek-text-resources
```

### MySQL Database

An externally-hosted MySQL (or MariaDB) database can be used instead of Django's built-in SQLite3 database.
Similar to the AWS bucket configuration, the following environment variables must be set:

| Variable | Description |
| --- | --- |
| `DB_BACKEND` | Which database backend to use. `mysql` or `sqlite` |
| `DB_NAME` | Name of database in the MySQL server |
| `DB_USER` | Username for MySQL server |
| `DB_PASSWORD` | Password for MySQL server |
| `DB_HOST` | Hostname for the MySQL server. Should be `localhost` if hosted on the same machine |
| `DB_HOST` | Port number for the MySQL server. `3306` is the default MySQL port |

Example `source` script:

```bash
export DB_BACKEND=mysql
export DB_NAME=geek_text
export DB_USER=username
export DB_PASSWORD=password
export DB_HOST=localhost
export DB_PORT=3306
```

MySQL database must be created using UTF-8 in order to work with Django:

```sql
CREATE DATABASE db_name CHARACTER SET utf8;
```

### Seed Database

During local testing, it may be useful to have a good amount of data to
manipulate. Towards this goal, we've added utility commands within the
`manage.py`:

- `seed_db` - Add randomly-generated entities to DB
- `clear_db` - Wipe all entities from the local DB

These can be invoked by calling them as arguments to `manage.py`, for
example:

```bash
> pwd # geek-text-webapp/webapp
> python manage.py seed_db
```

### Running Project

The following requires that a virtual environment be created and set up for
the project. To do so, refer to the
[Pip & Python VirualEnv](#pip--python-virtualenv) instructions in this README.

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

### Linting

The repo is setup so that when installing requirements, the
[Pylint](https://www.pylint.org/) tool is installed. This enables
linting for the project. The linter runs automatically within our CI
pipeline on opened Pull Requests. To run it locally, run the following
from the root of the repo:

```bash
pylint {module_name}
```

Where `module_name` is a path to the directory containing the module to
lint. The `pylintrc` file in the root of repo contains some
configurations that are useful defaults for the project.

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

