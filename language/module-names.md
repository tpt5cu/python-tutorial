- https://www.python.org/dev/peps/pep-0008/
- https://stackoverflow.com/questions/26503509/is-pypi-case-sensitive
# Python module name rules
- Modules should have short, all-lowercase names. Underscores can be used in the module name if it improves readability. Python packages should also
  have short, all-lowercase names, although the use of underscores is discouraged.
    - Thus, hyphens are NOT ALLOWED. It's a syntax error in the code anyway
- pip is case insensitive. Hyphens and underscores are considered equivalent
- Numbers are allowed (e.g. urllib3)
# Other details
- When an extension module written in C or C++ has an accompanying Python module that provides a higher level (e.g. more object oriented) interface,
  the C/C++ module has a leading underscore (e.g. _socket).