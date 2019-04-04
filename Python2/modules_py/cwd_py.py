"""
https://stackoverflow.com/questions/5137497/find-current-directory-and-files-directory
"""

import os

"""
The current working directory is set to the same directory from which $ python $ is run.
The cwd is used to resolve relative file paths, such as "../../.gitignore". Thus, a relative file path can fail/succeed entirely based on where $ 
python $ is run.
"""

def view_cwd():
    print("The cwd is: " + os.getcwd())

if __name__ == "__main__":
    view_cwd()