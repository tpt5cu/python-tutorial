#https://docs.python.org/2/library/datetime.html


from datetime import datetime


def invalid_year():
    """
    datetime arguments have the following allowable ranges:
    - MINYEAR (1) <= year <= MAXYEAR (9999)
    - 1 <= month <= 12
    - 1 <= day <= number of days in the given month and year
    - 0 <= hour < 24
    - 0 <= minute < 60
    - 0 <= second < 60
    - 0 <= microsecond < 1000000
    """
    #dt = datetime(10000, 1, 1) # Throws ValueError
    dt = datetime(9999, 1, 1)
    print(dt)


if __name__ == "__main__":
    invalid_year()