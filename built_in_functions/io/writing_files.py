# https://stackoverflow.com/questions/6159900/correct-way-to-write-line-to-file


def get_parent_dir_path(target_dir):
    # It should be a valid string, but if it's not then an error will (correctly) be thrown
    target_dir = str(target_dir)
    if not target_dir.endswith("/"):
        target_dir += "/"
    # Get the absolute path of this module
    this_module = str(__file__)
    # Get the index where the target_dir ends in the path
    idx = this_module.find(target_dir) + len(target_dir)
    # slice the path to get the part I want
    path = this_module[:idx]
    # print(this_module)
    # print(path)
    return path


def write_lines():
    with open(get_parent_dir_path("python-tutorial") + "temp.txt", mode="w", encoding="utf-8") as file:
        for x in range(100):
            file.write(str(x) + "\n")
    print("File was overwritten")


if __name__ == "__main__":
    # get_parent_dir_path("python-tutorial/")
    write_lines()
