# https://www.journaldev.com/23365/python-string-to-datetime-strptime

from datetime import datetime


def string_to_datetime():
    """strptime() converts a string into a datetime object"""
    # Here is a list of dictionaries
    allData = [
        {'meterid,timestamp,power,pf': '471135,01/01/2011 00:00:00,1015.74,1.0'},
        {'meterid,timestamp,power,pf': '471135,01/01/2011 01:00:00,1015.74,1.0'},
        {'meterid,timestamp,power,pf': '471135,01/01/2011 02:00:00,1010.34,1.0'},
        {'meterid,timestamp,power,pf': '471135,01/01/2011 03:00:00,1010.88,1.0'}
    ]
    firstDateTime = datetime.strptime(allData[1]["timestamp"], "%m/%d/%Y %H:%M:%S")


if __name__ == "__main__":
    string_to_datetime()