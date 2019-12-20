# https://stackoverflow.com/questions/714063/importing-modules-from-parent-folder/50194143#50194143 - introduction to using setuptools 
# https://stackoverflow.com/questions/1550226/python-setup-py-uninstall


'''
Install package

- $ pip install -e .
    - This installs my package, NOT $ python setup.py
- Make sure every directory has an __init__.py file (for Python 2)
    - The directory within which this setup.py file is should NOT have an __init__.py file
    - I can just re-run this file and add more __init__.py files as needed. I don't have to add an __init__.py file to every directory right now
- If a virtualenv is active when this file is run, then this package will only be installed under the virtualenv
- The name of the project is "python2_tutorial", but each directory under the "python_27" directory is its own top-level package and must be imported
  as such

Uninstall package

'''


from setuptools import setup, find_packages
setup(name='python2-tutorial', version='1.0', packages=find_packages())