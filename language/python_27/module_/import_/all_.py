# https://stackoverflow.com/questions/44834/can-someone-explain-all-in-python


'''
TLDR: __all__ really only matters when using the "import *" syntax, which isn't recommended

- __all__ is an optional special variable inside of __init__.py 
- If __all__ exists, then:
    - It is a list of strings that defines which symbols (e.g. functions, classes, variables, etc.) will be exported when "from <module> import *" is used
        - Everything not mentioned in __all__ WON'T be exported with the import * syntax
        - Anything not mentioned in __all__ can still be imported normally
- If __all__ doesn't exist (or is commented out), then:
    - "from <module> import *" will import ALL symbols from the module that do NOT being with an underscore
'''