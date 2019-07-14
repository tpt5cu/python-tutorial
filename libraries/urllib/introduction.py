# https://docs.python.org/2/library/urllib.html
# https://docs.python.org/3.1/howto/urllib2.html


import urllib, re, csv, os


"""
Unfortunately, urllib does not work with multiprocessing on macOS either. Apparently this whole fork() issue is with macOS, not Python. See
https://bugs.python.org/issue33725
"""


def get_data():
    # This returns a file-like object
    r = urllib.urlopen("https://www1.ncdc.noaa.gov/pub/data/uscrn/products/hourly02/2018/CRNH0203-2018-CO_Dinosaur_2_E.txt")
    # This gets the page as a string
    html = r.read() 
    # This works as expected
    rows = [re.split("\s+", line) for line in html.splitlines()]
    filepath = os.path.join(os.path.dirname(__file__), "test-csv.csv")
    with open(filepath, 'w') as f:
        writer = csv.writer(f)
        writer.writerows(rows)


if __name__ == "__main__":
    get_data()