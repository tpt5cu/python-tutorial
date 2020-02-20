# https://stackoverflow.com/questions/3518778/how-do-i-read-csv-data-into-a-record-array-in-numpy

import pathlib
import numpy
import pandas as pd


'''TLDR: pandas is better for this than numpy'''


def numpy_read_csv():
    '''
    - The "delimiter" parameter is what makes the function read a csv properly
    - dtype=None makes numpy determine the dtype of each individual column
        - dtype can be set to an iterable, but it doesn't work like I want
    - "encoding" defines the encoding used to decode the entire input file
    '''
    p = pathlib.Path(__file__).parent / 'data.csv'
    # This creates a single list of tuples for some reason
    #data = numpy.genfromtxt(p, delimiter=',', dtype=None, encoding='utf-8')
    # This works, but it's annoying that everything is a str
    data = numpy.genfromtxt(p, delimiter=',', dtype=str, encoding='utf-8')
    # This doesn't work like I want it to
    #data = numpy.genfromtxt(p, delimiter=',', dtype=[str, int, str], encoding='utf-8')
    print(data)


def pandas_read_csv():
    '''
    - Use "quotechar" to get rid of quotes around string data if they exist. Very convenient!
    - Pandas will use the first row of the csv as headers, unless I specify otherwise
    '''
    p = pathlib.Path(__file__).parent / 'data.csv'
    df = pd.read_csv(p, quotechar="'")
    print(type(df)) # <class 'pandas.core.frame.DataFrame'>
    # Get all rows of the first column, then convert the retrieved Series into an ndarray
    lifespans = df.iloc[:, 1].to_numpy()
    print(type(lifespans)) # <class 'numpy.ndarray'>
    print(lifespans) # [15 12 10  1]


if __name__ == '__main__':
    #numpy_read_csv()
    pandas_read_csv()
