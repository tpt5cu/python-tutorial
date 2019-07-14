import shutil, os


def remove_directory_tree():
    """
    Attempting to remove a nonexistent directory raises an OSError with errno == 2. rmtree() will delete all subdirectories if their parent directory
    is deleted.
    """
    dir_path = os.path.join(os.path.dirname(__file__), "parent")
    shutil.rmtree(dir_path)


if __name__ == "__main__":
    remove_directory_tree()