def get_project_route_path():
    target_dir = "python_tutorial"
    if not target_dir.endswith("/"):
        target_dir += "/"
    this_module = str(__file__)
    # idx = the index of the end of the substring: "python_tutorial/"
    idx = this_module.find(target_dir) + len(target_dir)
    # Get the full absolute path that includes "python_tutorial/"
    path = this_module[:idx]
    return path


if __name__ == "__main__":
    print(get_project_route_path())
