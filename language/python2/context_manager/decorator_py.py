from contextlib import contextmanager


@contextmanager
def increment_number():
    """
    A generator function can be decorated to become a context manager. Everything before the "yield" statement is __enter__() and everything after the
    "yield" statement is __exit__. Super easy!
    """