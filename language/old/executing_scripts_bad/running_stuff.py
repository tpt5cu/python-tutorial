# https://docs.python.org/2/using/cmdline.html#cmdoption-m (documentation on command-line, yes I use CPython)
# https://stackoverflow.com/questions/22241420/execution-of-python-code-with-m-option-or-not


def hello(arg="default"):
    print("hello there!")
    print(str(arg))
    print(__file__)