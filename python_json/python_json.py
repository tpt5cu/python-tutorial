# https://realpython.com/python-json/
# https://docs.python.org/3/library/json.html

import json


def serialize_python():
    """In this context, serialization means writing Python data into json which is then either 1) transferred across
    the network or 2) written to a file or 3) used as-is.

    There are lots of optional arguments for determining the exact presentation of the json.

    This is a Python dictionary. The json library maps between Python data types and json types. Dictionaries are
    mapped to json objects. If a type does not have a mapping to json, then it isn't serializable and an error
    will be thrown. To fix this, create a custom encoding function and pass this to json.dump()
    """
    classes = {
        "Math": "Calculus 1",
        "History": "Chinese Ancient History",
        "Science": "Physics 2",
        "Elective": "Advanced Chorus"
    }
    with open("output.json", mode="w", encoding="utf-8") as file:
        json.dump(classes, file, indent=4)

    """json.dumps() simply serializes the obj to a Python string that is also formatted as valid json,
    as supposed to writing the json to a file.
    """
    json_string = json.dumps(classes)
    print(json_string)


def deserialize_json():
    """Deserialization is NOT a perfect inverse of serialization. If a serialize an object, I might not get EXACTLY
    the same object back when it's deserialized.

    There is a mapping between json types and Python types. json.load() will return a data type
    that is dependent on the mapping between json and Python types.
    """
    with open("source.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    print(type(data))
    print(data)

    """json.loads() does the same exact thing as json.load(), except that json.loads() expects an actual Python string
    (which must also be valid formatted json) as its argument.
    """
    json_data = """ 
        {
            "researcher": {
                "name": "Ford Prefect",
                "species": "Betelgeusian",
                "relatives": [
                    {
                        "name": "Zaphod Beeblebrox",
                        "species": "Betelgeusian"
                    }
                ]
            }
        } 
    """
    string_data = json.loads(json_data)
    print(type(string_data))
    print(string_data)


if __name__ == "__main__":
    #serialize_python()
    deserialize_json()