import shutil


def nonexistant_dir():
    """ Attempting to delete a non-existant directory tree throws an OSError """
    shutil.rmtree("./hello")


if __name__ == "__main__":
    nonexistant_dir()