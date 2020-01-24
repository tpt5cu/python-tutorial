# https://stackoverflow.com/questions/51300181/is-it-necessary-to-call-flush-method-of-file-handler-in-python


'''
TLDR: flush() is only necessary when 1) the file hasn't been closed yet and 2) some other thread or process needs to read the contents of a file that
is still being written to
'''