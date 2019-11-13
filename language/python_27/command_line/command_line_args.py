import sys


def view_command_line_args():
    """sys.argv[0] is always the name of the script."""
    count = 0
    for e in sys.argv:
        print("sys.argv[{}] was {}".format(count, e))
        count += 1


if __name__ == "__main__":
    view_command_line_args()