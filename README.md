# Gramps Online

A simple, online version of [Gramps](https://gramps-project.org/).

## Project vision

This project aims to produce a platform for collaborating on a shared genealogy network/graph. It should allow many people to edit the tree and keep track of changes.

The genealogy data should be made visible via intuitive and interactive graphical representations, to facilitate human understanding of our heritage.

The data produced through this collaborative process should be publicly accessible, part of our commonwealth, while respecting privacy of living persons.

## Design principles

The following principles guide decisions for design and development of this project.

- usability is paramount
  - it may be good to sacrifice some flexibility, so that end-users have an easy time
- write Pythonic code
  - e.g. follow the [Zen of Python](https://www.python.org/dev/peps/pep-0020/)
- follow well-documented Django conventions

## Development

This section outlines how to set up a basic development environment. If you have any difficulties, feel free to [open an issue](https://github.com/gramps-project/gramps-online/issues/new). We will gladly help!

### Prerequisites

In order to set up a developer environment, you will need to have [Python 3](https://www.python.org/), [PostGIS](https://postgis.net/) (with Python 3 bindings), and [Git](https://git-scm.com/) installed on your computer.

#### Python 3

[Download Python 3](https://www.python.org/downloads/) from the official website, or install it via the package manager for your operating system.

#### Neo4j

Refer to the official Neo4j documentation for [installing Neo4j](https://neo4j.com/docs/operations-manual/3.5/installation/).

#### Git

You can [download git from the official website](https://git-scm.com/downloads). Additionally, there are a number of [Graphical User Interfaces for Git](https://git-scm.com/downloads/guis), that make it a bit easier to learn and use.

### Project source code and dependencies

With the basic software installed, you can set up a development environment with the following steps.

1. clone this repository to a working directory of your choice
   - `git clone git@github.com:gramps-project/gramps-online.git`\
2. change into the cloned directory
   - `cd gramps-online` (Linux and Mac)
3. create a [Python 3 virtual environment](https://docs.python.org/3/library/venv.html) (for good housekeeping)
   - `python3 -m venv venv` this will create a folder named `venv` with a virtual environment
4. activate the virtual environment
   - `source venv/bin/activate` (Linux and Mac)
5. install the project dependencies

   - `pip3 install -r requirements.txt`

### Initial database configuration

You will now need to run a few commands to set up initial database tables and an administrative user.

1. set up the database tables
   - `python3 manage.py migrate`
2. create an initial super user (administrative user)
   - `python3 manage.py createsuperuser`

At this point, you are ready to run the django server and start development!

### Running the project

Once you have installed the project, by following the steps above, you can run the project with the following command:

`DJANGO_USE_DEBUG=True python manage.py runserver`

The project should now be running. Happy hacking!
