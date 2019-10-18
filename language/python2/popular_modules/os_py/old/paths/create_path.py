# https://medium.com/@ageitgey/python-3-quick-tip-the-easy-way-to-deal-with-file-paths-on-windows-mac-and-linux-11a072b58d5f


import os


def windows_vs_unix():
    """
    The open() function will implicitly convert between '/' (Unix path separator) and '\' (Windows path separator), so I can hardcode Unix paths and
    it will run fine on Windows. However, Python libraries are guaranteed to also follow this behavior, so best practice is to NEVER hardcode ANY path
    separators into my code
    """
    # This is bad
    #filepath = os.path.join(os.path.dirname(__file__), "../os_py/create_file_path.py")
    # This is good
    filepath = os.path.join(os.path.dirname(__file__), '..', 'os_py', 'create_file_path.py')
    with open (filepath) as f:
        print(f.read())


def join_paths():
    """os.path.join() merely joins path and stops at the first absolute path. It does not eliminate redundant slashes."""
    # None of these paths is a absolute path. Therefore, the final resulting path is a relative path
    print(os.path.join("hello", "my", "name", "is", "Austin")) # hello/my/name/is/Austin
    # This function joins from right to left. As soon as the rightmost absolute path is found, everthing to the left of it is thrown away and
    # everything to the right of it is joined to it
    print(os.path.join("hello", "my", "/name", "is", "Austin")) # /name/is/Austin
    print(os.path.join("hello", "/my", "/name", "is", "Austin")) # /name/is/Austin
    print(os.path.join("hello", "my", "name", "/is", "Austin")) # /is/Austin

    # IOError: not a directory. It must be illegal to try and navigate backwards from a filepath
    #filepath = os.path.join(os.path.abspath(__file__), "../introduction.py")
    #print(filepath) # '/Users/austinchang/tutorials/python/language/python2/popular_modules/os_py/paths/create_path.py/../introduction.py'

    # This works fine. It is fine to navigate backwards with a directory
    filepath = os.path.join(os.path.dirname(__file__), "../introduction.py")
    print(filepath) # /Users/austinchang/tutorials/python/language/python2/popular_modules/os_py/paths/../introduction.py

    with open(filepath) as f:
        print(f.read())


if __name__ == "__main__":
    #windows_vs_unix()
    join_paths()