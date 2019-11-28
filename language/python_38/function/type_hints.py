# https://www.python.org/dev/peps/pep-0484/
# https://realpython.com/python-type-checking - there's some deep theory here


'''
Do I want to use type hints? Maybe for code that other people are looking at it could be useful.
- Use type hints over type comments when possible
- I would only ever want to use the typing module to add type hints after 1) I've written 100% of the code 2) the code has been tested and iterated
  over several times 3) it's going to be used by other people
- Don't even try if someone else will have to maintain or change the code later who doesn't understand type hints. It will just confuse everyone and
  probably introduce inconsistencies between the hints and the code. Type hints can get crazy and begin to require lots of mental effort, especially
  with custom classes
'''


def build_app(name: str, version: float) -> dict:
    '''
    - Type hints were added in 3.5
        - Type comments were back-ported to Python 2.7
    - Type hints don't force Python to enforce type checking.
    - Some argue type hints are worth writing when unit tests are worth writing
    - Note how the colon goes after the arrow
    '''
    print(f'Congratulations on building your app "{name}", version {version}')
    return {
        'name': name,
        'version': version
    }


if __name__ == '__main__':
    build_app('Swimmy Fish', 0.1)
    build_app([5], bytes())
    # Functions store their annotations
    print(build_app.__annotations__) # {'name': <class 'str'>, 'version': <class 'float'>, 'return': <class 'dict'>}
    # Starting is 3.6, variables can be annotated too
    date: str = 'Today'
    print(date)
    # A module stores its annotations too
    print(__annotations__) # {'date': <class 'str'>}