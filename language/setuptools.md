- https://stackoverflow.com/questions/38164587/format-of-name-of-a-python-package-with-setuptools
# setuptools distribution name rules
- No spaces
- Names are case-insensitive
- Numbers, periods, hypthens, and underscores are allowed
- Hyphens and underscores are equivalent
# Importing a setuptools package
- The setuptools distribution name is irrelevant
- Whatever directory contains "setup.py" ITSELF contains the ROOT(S) of the setuptools package
    - E.g. If setup.py is in `/Users/austinchang/tutorials/python/language/python_369/`, then `import python3_tutorial` will never work, but all of
      these work:
    ```
    import exceptions_
    import popular_modules
    import print_
    ```
# Install a setuptools package
- $ pip install -e .
    - Looks for setup.py in the current directory and installs the package
    - The -e flag installs the project in an editable state so that changes to files are automatically available in the package
- Python 3: any (non-hidden) directory that is in the directory of setup.py will be treated as a Python package
- Python 2: Make sure every directory that is supposed to be a top-level package has an __init__.py file, otherwise it won't be a top-level package
  and none of its subdirectories will be packages either
# Uninstall a setuptools package
- Don't just delete the .egg-info directory. Uninstall properly with `pip uninstall <setuptools distribution name>`
## Uninstall a previously installed package (macOS)
- $ [sudo] python setup.py install --record `<filename>`
    - Record the list of installed files inside of `<filename>`
    - This command will:
        - Definitely create a build/ and a dist/ directory
        - Probably 1) fail with permission denied 2) not write `<filename>` because it failed
            - It will probably fail because the new (non-sudo) installation will find files that were left over from the sudo installation
    - Tried running it with sudo
        - It worked. `<filename>` was written
        - For a trivial installation, it appears that only a .egg file was created deep within a venv
        - Removed the file and the top-level .egg-info directory
        - Tried non-sudo reinstall, but it failed due to a .pth file
            - Removed that file too
        - The non-sudo setup.py installation now works!
- When the above command is run with a complex installation, a whole host of files are output
    - Remove them with:
        - $ cat files.txt | xargs printf $'\'%s\'\n' | xargs sudo rm
## Problems
- Permission denied
    - Making setup.py executable did not help
    - Interesting. The owner of omf.egg-info is root. This happens when $ pip install -e . $ (or I presume whatever other setup.py "installation"
      commands can be run) is run with sudo
        - drwxr-xr-x  8 root  staff  256 Sep 25  2018 omf.egg-info//