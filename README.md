# cell_counting
We create machine learning algorithm to count cells in the microscopy photo

# Environment setup

## virtualenv

One of the strengths of python is the plethora of libraries available via `pip install`. The
downside of this is that multiple projects use multiple versions of different libraries, and often
require specific versions that can then break other programs. This is where virtualenvs come
to the rescue. A virtualenv is a sort of playground where python libraries (and versions) can
be installed, but will in no way effect the system wide installed libraries or other virtualenvs.

### Command line use

To make things easier, it's highly recommended to use [virtualenv_wrapper](https://virtualenvwrapper.readthedocs.io/en/latest/).
This allows one to make a new virtualenv via:

    mkvirtualenv <name of virtualenv> --python=<path to python executable>

An example would be as below (change the path to wherever you installed python to):

    mkvirtualenv cells --python=/usr/bin/python3

This now allows you to call `workon cells` and any python calls will use your new virtualenv.
To exit a virtualenv, use `deactivate`.

### Pycharm usage

Pycharm aims to handle all such things via it's interface - therefore a new virtualenv
can be created and setup for a given project via 'project -> preferences -> interpreter'.

## Dependencies

Any decent python project will have a load of external dependencies, i.e. libraries
which it needs to work. These are installed via `pip`, but it would be bothersome
to have to manually type `pip install bla` for each library. To get around this,
a special requirements file is kept which specifies each required library along with
the version it should have. To install all requirements, simply run the following (of
course in a virtualenv):

    pip install -r requirements.txt
