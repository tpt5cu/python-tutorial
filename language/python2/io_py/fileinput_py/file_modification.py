import os, fileinput

def inplace():
    """
    When fileinput.input() is used as the interface to the module, a global fileinput instance is created that is shared across all method invocations
    of the module.
    Using the inplace flag 1) adds the ".bak" extension to the original file and 2) creates a new file with the same original filename.
    The backup file is iterated over and any modifications are written to the new file (which looks like the original file). The backup file is
    deleted at the end of the operation. 
    Each line is returned with its newline at the end during iteration.
    """
    filepath = os.path.join(os.path.dirname(__file__), "testCsv.csv")
    for line in fileinput.input(filepath, inplace=1):
        if fileinput.filelineno() % 2 == 0:
            # fileinput maps stdout to the file being iterated over, so use print to modify the file
            print "Even line number: " + str(fileinput.filelineno())
        else:
            # When this line is printed, its newline is printed AND print inserts another newline. I can avoid this by either stripping off the
            # newline or modifying the print invocation
            print line.rstrip("\n")

def write_new_file():
    """
    When the inplace flag isn't used, stdout is not redirected back into the file so any print statements just appear in the console.
    To write one file into another, I should use a combination of open and fileinput. fileinput is made for processing lots of files conveniently.
    It's not made for writing to files. The inplace modification ability is nice, but not sufficient for writing new files.
    """
    filepath = os.path.join(os.path.dirname(__file__), "testCsv.csv")
    new_filepath = os.path.join(os.path.dirname(__file__), "cool-new-file.csv")
    # The 'w' flag is correct. The file is opened once, and only at that point is anything overwritten. I don't need to use the 'a' flag.
    with open(new_filepath, 'a') as f:
        for line in fileinput.input(filepath):
            f.write(line) 

    
if __name__ == "__main__":
    #inplace()
    write_new_file()
