# https://realpython.com/python-dicts/
# https://stackoverflow.com/questions/9415785/merging-several-python-dictionaries


import json


'''
A dictionary is another mutable collection, like a list, except that data is stored and accessed in key-value pairs. Dictionaries do NOT keep order
(well, starting in Python 3.7 they do), so don't depend on the insertion order of a dictionary. I think that dictionary keys can be of any immutable
type
'''


def literal():
    foods = {
        'starch': 'bread',
        'protein': 'steak',
        'dairy': 'yogurt'
    }
    print(foods)
    # Dictionaries might look like JavaScript objects, but they are not. All keys must have a defined type. Keys are not automatically strings.
    #animals = {
    #    cat: "Molly",
    #    dog: "george"
    #}
    #print(animals)


def fill_with_keys():
    '''Create a dict with specified keys, where each key holds a different (yes different) list.'''
    keys = ['a', 'b', 'c']
    d = {key:[] for key in keys}
    d['a'].append('foobar')
    print(d)


def merge_dicts():
    '''The fact is that a dictionary cannot be unpacked into a dictionary that already exists'''
    d1 = {'direction': 'right', 'color': 'maroon'}
    d2 = {'weather': 'sunny'}
    # Only allowed in Python 3
    #d3 = {**d1, **d2}
    # Only allowed in Python 3
    #d3 = {**d1}
    # Doesn't work
    #d3 = {k: d1[k] for k in d1}
    d3 = {}
    for k in d1:
        d3[k] = d1[k]
    for k in d2:
        d3[k] = d2[k]
    print(d3)


def convert_from_and_to_string():
    '''This isn't a tricky problem. Just use json.dumps() and json.loads()'''
    d = {
        'name': 'latitude',
        'value': None,
        'subkey': {
            'name': 'wind speed',
            'values': [1, 2, None]
        }
    }
    s = json.dumps(d)
    print(s) # {"name": "latitude", "value": null, "subkey": {"values": [1, 2, null], "name": "wind speed"}}
    print(json.loads(s)) # {u'name': u'latitude', u'value': None, u'subkey': {u'values': [1, 2, None], u'name': u'wind speed'}}


if __name__ == "__main__":
    #literal()
    #fill_with_keys()
    merge_dicts()
    #convert_from_and_to_string()