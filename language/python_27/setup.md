- https://setuptools.readthedocs.io/en/latest/setuptools.html#egg-info-create-egg-metadata-and-set-build-tags
- https://stackoverflow.com/questions/1550226/python-setup-py-uninstall
# Install package
- $ pip install -e .
    - Looks for setup.py in the current directory and installs the package
    - The -e flag installs the project in an editable state so that changes to files are automatically available in the package
- Make sure every directory that is supposed to be a top-level package has an __init__.py file, otherwise it won't be a top-level package and none of
  its subdirectories will be packages either
# Uninstall a previously installed package (macOS)
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

    
# egg_info
- egg_info is a command that primarily is used to update a projects .egg-info metadata directory
- Invocation: $ python setup.py egg_info
## Problems
- Permission denied
    - Making setup.py executable did not help
    - Interesting. The owner of omf.egg-info is root. This happens when $ pip install -e . $ (or I presume whatever other setup.py "installation"
      commands can be run) is run with sudo
        - drwxr-xr-x  8 root  staff  256 Sep 25  2018 omf.egg-info//