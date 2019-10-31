# https://docs.python.org/2/library/json.html


import json, os

dictionary = {
    'name': 'AG_1000CUEPR',
    'conductor_resistance': '0.088 ohm/kft',
    'object': 'underground_line_conductor',
    'shield_resistance': '0.0000 Ohm/mile',
    'neutral_gmr': '0.0037 ft',
    'outer_diameter': '1.6600 in',
    'neutral_strands': '26.0000',
    'neutral_resistance': '4.6758 ohm/kft',
    'neutral_diameter': '0.1144 in',
    'conductor_diameter': '1.117 in',
    'shield_gmr': '0.0000 ft',
    'conductor_gmr': '0.0393 ft'
}

def write_to_file():
    """
    The json.dump() function writes the Python data to the selected file. There are many options for exactly how the file is written. The file is
    written as JSON. By that I mean the entire file is not enclosed in quotations.
    - 
    """
    filepath = os.path.join(os.path.dirname(__file__), 'output.json')
    with open(filepath, 'r+') as f:
        f.truncate()
        # This writes a string to the file, since a string is a valid JSON type. However, it is only coincidental that the string also happens to be
        # valid JSON
        #json.dump(str(dictionary), f, indent=4) 
        # This writes a Python object to the file. The object is written in JSON, not a string
        json.dump(dictionary, f, indent=4)

def write_to_string():
    """
    json.dump() and json.dumps() seem the same, but they are completely different. json.dumps() simply serializes the obj to a Python string that is
    also formatted as valid json, as opposed to writing the json to a file.
    """
    print(json.dumps(dictionary, indent=4))

if __name__ == "__main__":
    write_to_file()
    #write_to_string()