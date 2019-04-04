# https://docs.python.org/2/library/csv.html
# https://en.wikipedia.org/wiki/Escape_sequences_in_C

import csv
from my_helper_package import helper_functions


def read_csv_file_to_dictionary():
    """DictReader() returns a reader object, which is an iterator. The reader object will iterate over each line
    of whatever iterable was passed to DictReader().
    DictReader() is special because not only does it read each line, it maps each line to a dictionary.
    DictReader() is just a wrapper over the standard reader.
    A reader can accept a bunch of kwargs described in
    "13.1.2. Dialects and Formatting Parameters", including a delimiter.
    """
    file_path = helper_functions.get_project_route_path() + "testCsv.csv"
    count = 0
    with open(file_path) as csv_file:
        reader = csv.DictReader(csv_file)
        # This line below is not what I want
        #reader = csv.DictReader(csv_file, delimiter='\t')
        for row in reader:
            count += 1
            if count < 20:
                print(row)
                #print(row["timestamp"])
                #print(row["meterid"])
                #print(row["pf"])
                #print(row["power"])
            else:
                break


if __name__ == "__main__":
    read_csv_file_to_dictionary()
