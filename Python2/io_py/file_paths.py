import os

def resolve_relative_path():
    """ I should not use relative paths when opening files because the relative path will be resolved according to the cwd, which is set by where $ 
    python $ is run. 
    I should not use absolute paths because then no other machine will be able to run my code.
    Instead, I should use the os.path module
    """
    # This is bad
    #with open("../../.gitignore") as f:
        #print(f.readlines())
    # This is bad
    #with open("/Users/austinchang/tutorials/python/.gitignore") as f:
        #print(f.read())
    # This is good. It will work anywhere.
    with open(os.path.join(os.path.dirname(__file__), "../../.gitignore")) as f:
        print(f.read())

if __name__ == "__main__":
    resolve_relative_path()