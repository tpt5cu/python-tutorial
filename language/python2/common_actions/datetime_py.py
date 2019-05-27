"""
https://stackoverflow.com/questions/13703720/converting-between-datetime-timestamp-and-datetime64
"""

"""
If I ever see a datetime object like '2017-06-01 00:00:00-05:00', then:
- '2017-06-01' is year-month-day
- '00:00:00' is hrs-mins-secs
- '-05:00' is 5 hours subtracted from UTC, which represents EST (Eastern Standard Time), which starts in November and ends in March
    - '-04:00' is 4 hours subtracted from UTC, which represents EDT (Eastern Daylight Time), which starts in March and ends in November
"""