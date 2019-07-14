# https://pandas.pydata.org/pandas-docs/stable/reference/groupby.html - Pandas GroupBy object
# https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.groupby.html - DataFrame groupby() method


import datetime, re
import numpy as np
import pandas as pd


"""By default, groups are sorted by their group names in the groupby() operation. Set groupby(sort=False) to avoid this."""


def get_datetime_by_meter_dataframe():
    """
    7 days by 10 meters. Each day has 2 measurements: 12am and 12pm.
    Weekends: 3-4, 
    Weekdays: 1-2, 5-7
    """
    start_date = datetime.datetime(2017, 6, 1)
    day = datetime.timedelta(hours=12)
    df = pd.DataFrame(
        np.array([
            np.full((10,), 1), # Thur
            np.full((10,), 2), # Thur
            np.full((10,), 1), # Fri
            np.full((10,), 2), # Fri
            np.full((10,), 3), # Sat
            np.full((10,), 3), # Sat
            np.full((10,), 4), # Sun 
            np.full((10,), 4), # Sun
            np.full((10,), 1), # Mon
            np.full((10,), 2), # Mon
            np.full((10,), 1), # Tue
            np.full((10,), 2), # Tue
            np.full((10,), 1), # Wed
            np.full((10,), 2), # Wed
        ]),
        index=[start_date + day * x for x in range(14)],
        columns=["Meter1", "Meter2", "Meter3", "Meter4", "Meter5", "Meter6", "Meter7", "Meter8", "Meter9", "Meter10"]
    )
    return df


def group_by_function():
    """
    The result of grouping by a function is a dictionary. The keys of the dictionary are the names of the groups themselves. The value at each key is
    some form of sequence of the index labels or column labels assigned to a group. By default, groupby() applies the grouping function to row labels
    (axis=0). To group by column labels, I must set (axis=1)
    """
    df = get_datetime_by_meter_dataframe()
    print(df)
    print()
    day_groupby = df.groupby(lambda dt: dt.day <= 4)
    print(day_groupby.groups)
    print(type(day_groupby.groups)) # <class 'dict'>
    print()
    column_groupby = df.groupby(lambda meter_name: int(re.search("\d+", meter_name).group()) <= 5, axis=1)
    print(column_groupby.groups)
    print()
    week_groupby = df.groupby(lambda dt: "Weekend" if dt.day == 3 or dt.day == 4 else "WeekDay")
    print(week_groupby.groups)
    print()
    print(week_groupby.groups["WeekDay"][0])


#def group_by_levels():
#    """If strings are passed to groupby, the strings can refer to column levels or index levels."""
#    df = get_datetime_by_meter_dataframe()
#    column_groups = df.groupby(["Meter1", "Meter2"], axis=1)
#    for g in column_groups:
#        print(g)
#        print()


def group_by_day():
    """
    <GroupBy>.aggregate(<func>) applies the function <func> to each group in <GroupBy>.
    - If a group only groups by row levels (and not column levels), then the function will apply to all the rows in a particular column. In other
      words, the aggregation will be performed on each column, and the original columns will remain distinct from each other.
    - <GroupBy>.aggregate() and <GroupBy>.agg() are the same thing.
    """
    df = get_datetime_by_meter_dataframe()
    week_groupby = df.groupby(lambda dt: "Weekend" if dt.day == 3 or dt.day == 4 else "WeekDay")
    print(df)
    print()
    print(week_groupby.groups)
    print()
    #print(week_groupby.aggregate(np.sum)) # sum each group in a column
    print(week_groupby.mean()) # compute the mean of each group in a column


def group_by_day_transposed():
    """This works just like group_by_day() as expected."""
    df = get_datetime_by_meter_dataframe()
    df = df.transpose()
    week_groupby = df.groupby(lambda dt: "Weekend" if dt.day == 3 or dt.day == 4 else "WeekDay", axis=1)
    print(df)
    print()
    print(week_groupby.groups)
    print()
    print(week_groupby.mean()) # compute the mean of each group in a column


def group_by_day_and_time():
    def grouping_function(dt):
        weekdays = [1, 2]
        weekdays.extend(range(5, 10))
        weekdays.extend(range(12, 17))
        weekdays.extend(range(19, 24))
        weekdays.extend(range(26, 31))
        if dt.day in weekdays:
            group_name = "weekday"
        else:
            group_name = "weekend"
        group_name += "-" + str(dt.hour) + ":" + str(dt.minute)
        return group_name
    df = get_datetime_by_meter_dataframe()
    print(df)
    print()
    gb = df.groupby(grouping_function)
    for g in gb:
        print(g)
    print()
    print(gb.mean())
    print(type(gb.mean())) # <class 'pandas.core.frame.DataFrame'>


def examine_grouped_columns():
    """I can use <DataFrame>.loc[<Index>] to view specific rows for all columns."""
    def grouping_function(dt):
        weekdays = [1, 2]
        weekdays.extend(range(5, 10))
        weekdays.extend(range(12, 17))
        weekdays.extend(range(19, 24))
        weekdays.extend(range(26, 31))
        if dt.day in weekdays:
            group_name = "weekday"
        else:
            group_name = "weekend"
        group_name += "-" + str(dt.hour) + ":" + str(dt.minute)
        return group_name
    df = get_datetime_by_meter_dataframe()
    print(df)
    print()
    gb = df.groupby(grouping_function)
    group = gb.groups[list(gb.groups)[1]]
    print(group)
    print()
    print(df.loc[group])
    print()
    print(gb.mean())


if __name__ == "__main__":
    #group_by_function()
    #group_by_levels()
    group_by_day()
    group_by_day_transposed()
    #group_by_day_and_time()
    #examine_grouped_columns()