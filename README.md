# gramps-online
A simple, online version of Gramps.

## Development
This section outlines how to set up a basic development environment. If you have any difficulties, feel free to open an issue. We will gladly help!

### Prerequisites
In order to set up a developer environment, you will need to have [Python 3](https://www.python.org/) and [Git](https://git-scm.com/) installed on your computer.

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

`python3 manage.py runserver`

The project should now be running. Happy hacking!