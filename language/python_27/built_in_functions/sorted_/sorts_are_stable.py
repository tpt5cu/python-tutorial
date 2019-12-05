# https://stackoverflow.com/questions/1915376/is-pythons-sorted-function-guaranteed-to-be-stable - sorted() and sort() are guaranteed to be stable,
# full stop


from built_in_functions.sorted_.introduction import custom_cmp_by_year, get_data


def sort_by_year_with_custom_cmp():
    '''
    Even though I'm using a custom cmp function, the sort IS stable. This makes sense, since stability is a property of the sorting algorithm, not the
    comparison function!

    Original:
        ['hourly', '2000', 'Alaska', 8760, 5000, 3760],
        ['hourly', '2001', 'Alabama', 8760, 4001, 4760],
        ['hourly', '2001', 'Maine', 8760, 2999, 5760],
        ['hourly', '2000', 'Maine', 8760, 3000, 5760],
        ['hourly', '2001', 'Alaska', 8760, 5001, 3760],
        ['hourly', '2001', 'Virginia', 8760, 4001, 4760],
        ['hourly', '2000', 'Virginia', 8760, 4000, 4760],
        ['hourly', '2000', 'Alabama', 8760, 4000, 4760
    Stable sorted:
        ['hourly', '2000', 'Alaska', 8760, 5000, 3760]
        ['hourly', '2000', 'Maine', 8760, 3000, 5760]
        ['hourly', '2000', 'Virginia', 8760, 4000, 4760]
        ['hourly', '2000', 'Alabama', 8760, 4000, 4760]
        ['hourly', '2001', 'Alabama', 8760, 4001, 4760]
        ['hourly', '2001', 'Maine', 8760, 2999, 5760]
        ['hourly', '2001', 'Alaska', 8760, 5001, 3760]
        ['hourly', '2001', 'Virginia', 8760, 4001, 4760]
    '''
    data = get_data()
    sorted_data = sorted(data, cmp=custom_cmp_by_year)
    for e in sorted_data:
        print(e)
        pass
    return sorted_data


if __name__ == '__main__':
    sort_by_year_with_custom_cmp()