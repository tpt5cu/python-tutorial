import json

"""
Turning JSON (which is always implicitly a string) into some data type in Python is called deserialization. Deserialization just means to convert a
string into something else. Deserialization is NOT a perfect inverse of serialization. If a serialize an object, I might not get EXACTLY the same
object back when it's deserialized.
"""

"""
There is a fixed mapping between JSON types and Python types.
json.loads() deserializes a STRING into a Python object.
json.load() deserializes a FILE POINTER into a Python object.
"""


def py_dict():
    """A JSON object is converted into a Python dictionary"""
    string = '{"researcher":{"name":"FordPrefect","species":"Betelgeusian","relatives":[{"name":"ZaphodBeeblebrox","species":"Betelgeusian"}]}}'
    dictionary = json.loads(string)
    print(type(dictionary))
    print(dictionary)


def py_list():
    """A JSON array is converted into a Python list"""
    string = "[1, 2.0, 3, 4]"
    my_list = json.loads(string)
    print(type(my_list))
    # The items with the JSON array are also mapped to their respective Python types. In this case, the numbers are converted into <int> and <float>
    print(type(my_list[0]))
    print(type(my_list[1]))
    print(my_list)


if __name__ == "__main__":
    #py_dict()
    py_list()
