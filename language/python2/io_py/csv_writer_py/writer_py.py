"""
https://docs.python.org/2/library/csv.html
"""


import os, csv


filepath = os.path.join(os.path.dirname(__file__), "my-csv.csv")
data = [
    [6, 2345, 7, 2345, 234],
    [15, 15, 456, 347, 1234],
    [46, 4, 45, 67, 2, 45, 35],
    [7, 87, 65, 872, 5, 5637, 34]
]


def basic_write():
    """ This is the simplest way to write with a csv writer """
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def examine_excel_dialect():
    """
    There are different CSV dialects across applications because there is no single CSV standard. A dialect is simply a grouping of certain format
    parameters. Examples of format parameters include the delimiter (defaults to ",") and how double quotes (") that appear inside data fields should
    be handled.
    - The only built-in dialects on my machine appear to be 'excel-tab' and 'excel'
    """
    print(csv.list_dialects()) # ['excel-tab', 'excel']
    print(dir(csv.excel)) # delimiter, doublequote, etc.
    print(csv.excel.delimiter) # ","


def write_header():
    """
    Only csv.DictWriter (as opposed to csv.writer) has writerows() method. To write a header row with csv.writer, just use the regular methods
    """
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        header = ["Header1", "Header2", "Header 3", "Header 4", "Header5"]
        writer.writerow(header)
        writer.writerows(data)


def write_strings():
    # This data behaves exactly as expected
    #data = [
    #    ["This", "is", "a", "sentence", "of", "words", "."],
    #    ["I", "like", "soft", "cake", "because", "it's", "subtle", "."],
    #    ["Red", "bananas", "look", "weird", "."]
    #]
    # This data is interpreted so that every character of a sentence is split into a csv datum! That's almost never what I want
    data = ["This is a sentence of words", "I like soft cake because it's subtle"]
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(data)


if __name__ == "__main__":
    #basic_write()
    #examine_excel_dialect()
    #write_header()
    write_strings()