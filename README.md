# Geek Text

_Book shopping site, with the right geek cred_

## Features
[List of main product features go here]

## Deploying

### Native

To try out the webapp on your own, clone this repo and run the following:

```bash
# Set up venv for repo
virtualenv --prompt=geek-text --python=python3 .venv
source .venv/bin/activate
pip install -r requirements.txt

# Run webapp
source .venv/bin/activate && cd webapp
python manage.py migrate
python manage.py runserver
```

More extensive information can be found in our [dev docs](dev/README.md).

### Docker-Compose

The project is set up so that the service can be run locally using
[Docker-Compose](https://docs.docker.com/compose/). Before running,
the required environment variables (see the [dev docs](dev/README.md))
must be active. A sample run is shown below:

```bash
# Setup Envirnoment
cp envfile.sample envfile
vim envfile # Fill in the variables listed in the file
source envfile

# Run Services
docker-compose build
docker-compose up
```

## Team

The following are the main developers of this project:

- [Dan Herrera](https://github.com/loksonarius)
- [Frank Hernandez](https://github.com/fhern077)
- [Jose Gonzalez](https://github.com/codeTony22)
- [Nico Gonzalez](https://github.com/FreakoNico)
- [Otto Gonzalez-Vega](https://github.com/ogonz110)

## Contributing

To develop on this project, please refer to the [Dev README](dev/README.md) for
info on getting started, contributing guidelines, and general orientation
information.

_This project is a school assignment for our Spring 2018 SoftEngI course_

