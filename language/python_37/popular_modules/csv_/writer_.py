# https://docs.python.org/3.7/library/csv.html
# http://python3porting.com/problems.html#csv-api-changes
# https://stackoverflow.com/questions/5358322/csv-modules-writer-wont-let-me-write-binary-out - Python 3 csv must be opened in text mode


import csv, os


'''
- The Python 3 csv module requires you to open the file in text-mode. It returns and expects Unicode strings.
    - "A row must be an iterable of strings or numbers for Writer objects"
    - This behavior should be way better documented, but it isn't!
- Always open a file with newline='' when using the csv module, regardless of platform
    - This is to handle newlines across platforms properly
'''


def write_text():
    '''Apparently I cannot open a file in binary mode for usage with the csv module in Python 3'''
    str_ = 'aaaàçççñññ'; print(type(str_)) # <type 'str'>
    with open(os.path.join(os.path.dirname(__file__), 'my-csv.csv'), 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerow(str_)


if __name__ == '__main__':
    write_text()