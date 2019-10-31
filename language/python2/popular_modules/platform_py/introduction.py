# https://docs.python.org/2/library/platform.html


import platform


def get_os():
    print(platform.system())


if __name__ == '__main__':
    get_os()