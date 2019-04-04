# https://stackoverflow.com/questions/19048732/python-setup-py-develop-vs-install

"""
The package directory(s) for a given Python interpreter can be found by running "import site; site.getsitepackages()" in the Python repl.

- The packages for the Homebrew installed Python 2.7 are located in /usr/local/lib/python2.7/site-packages
- The packages for the Homebrew installed Python 3 are located in /usr/local/lib/python3.7/site-packages

The omf package does not exist in either site-packages directory.
When I installed all of the omf stuff, I ran a command $ python2 setup.py develop
This command creates a special link between /Users/austinchang/pycharm/omf and the site-packages directory.
This special link IS the omf.egg-link file located in the site-packages directory for the Homebrew Python 2.7.
This special link treats the chosen folder AS a Python package. The special link makes it so that any changes
I make to my source code are immediately reflected in the omf package so I don't have to recompile the package
over and over again to use it.

It makes sense that pip recognizes omf as a package because of the special link file. But why does pip3 ALSO 
recognize the special link? For some reason, when I commented-out the PYTHON path setting in my .bash_profile file
(which pointed to both the omf source files and the python_tutorial source files), pip3 stopped listing omf as a package.
"""