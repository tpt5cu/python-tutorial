import json
import timeit
from performance.python_timeit import wrapper


def fast_parse(tree):
    # type: (dict) -> bool
    """Return True if the dictionary contains latitude and longitude data, otherwise False."""
    # If there is zero lat/lon info, do force layout by default.
    latLonCount = 0
    for key in tree:
        for subKey in ['latitude', 'longitude']:
            if subKey in tree[key]:
                latLonCount += 1
    if latLonCount == 0:
        return False
    return True


def slow_parse(tree):
    # type: (dict) -> bool
    """Return True if the dictionary contains latitude and longitude data, otherwise False."""
    lat_lon_count = 0
    for key in tree:
        sub_dict = tree[key]
        for sub_key in sub_dict:
            if sub_key == "latitude" or sub_key == "longitude":
                lat_lon_count += 1
    if lat_lon_count == 0:
        return False
    return True


def get_data():
    path = "/Users/austinchang/pycharm/omf/omf/static/publicFeeders/Simple Market System.omd"
    with open(path, "r") as f:
        thisFeed = {'tree': json.load(f)['tree']}
    tree = thisFeed['tree']
    #print(tree)
    return tree


def time_functions():
    tree = get_data()
    slow = wrapper(slow_parse, tree)
    fast = wrapper(fast_parse, tree)
    num = 100000
    print("fast is: " + str(timeit.timeit(fast, number=num)))
    print("slow is: " + str(timeit.timeit(slow, number=num)))

    
if __name__ == "__main__":
    """There must be something happening with caching but I don't know what."""
    time_functions()
