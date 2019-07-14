"""
https://matplotlib.org/3.1.0/api/dates_api.html
"""


"""
I want major ticks every hour, and minor ticks every 15 minutes. matplotlib doesn't care what my data actually represents. Even if my data is
correctly already in Python datetime.time() objects, matplotlib won't put the ticks where I want them by default.
"""

"""
The matplotlib.dates module contains special "Locator" classes. Recall that a "Locator" object is used to control the location of ticks on an Axis
object.
- YearLocator(): create ticks with a maximum frequency of once per year
- MonthLocator(): create ticks with a maximum frequency of once per month
- DayLocator(): create ticks with a maximum frequency of once per day
- HourLocator(): create ticks with a maximum frequency of once per hour
- AutoDateLocator(): picks the best DateLocator. Is this used by default?
"""


"""
- It also contains special "Formatter" classes. A "Formatter" object is used to control the text that appears above the ticks.
"""