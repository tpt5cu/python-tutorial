'''
It appears that comprehensions are much more powerful than I thought. I can freely navigate between sets, lists, and dictionaries however I want!
'''

def filter_dict():
    '''
    Using a for-loop inside of a dictionary comprehension just fills up a new dict with the same key-value pairs
    - Filtering is also possible, as shown here
    '''
    dict_ = {
        'name': 'Joe',
        'birthday': 'September',
        'age': 56
    }
    dict_copy = {k: dict_[k] for k in dict_}
    print(dict_ == dict_copy) # True
    print(dict_ is dict_copy) # False
    new_dict = {k: dict_[k] for k in dict_ if k != 'birthday'}
    print(new_dict) # {'age': 56, 'name': 'Joe'}


def accidentally_create_a_set():
    '''A set comprehension and a dict comprehension both use curly brackets'''
    dictionary = {
        "0": "2345q3",
        1: 4326423.45,
        "2": 1025.354
    }
    # This grabs the first 2 characters of every key
    my_dict = {key: str(dictionary.get(key))[0:2] for key in dictionary}
    print(my_dict) # {'0': '23', 1: '43', '2': '10'}
    # This returns a SET of the dictionary's keys
    my_dict = {key for key in dictionary}
    print(my_dict) # set(['0', '2', 1])


def list_to_dictionary():
    my_list = ["cat.omd", "person.omd", "class.omd"]
    # I am adding a useless "value" here, but I could do something else
    my_dict = {item[0:-4]: "value" for item in my_list}
    print(my_dict) # {'person': 'value', 'class': 'value', 'cat': 'value'}


def combine_dictionaries():
    '''
    inputDict should overwrite defaultInputs, except when inputDict has a None value
    '''
    inputDict = {
		"user": "Austin",
		"networkName1": "cool network",
		"algorithm": "mergesort",
		"model": None,
		"tolerance": None,
		"iteration": 9,
		"genLimits": None
	}
    defaultInputs = {
		"user": "admin",
		"networkName1": "case9",
		"algorithm": "NR",
		"model": "AC",
		"tolerance": "0.00000001",
		"iteration": 10,
		"genLimits": 0,
    }
    my_dict = {key: inputDict[key] if inputDict[key] is not None else defaultInputs[key] for key in inputDict}
    # This is an alternative
    for key in inputDict:
        if inputDict[key] is not None:
            defaultInputs[key] = inputDict[key]
    # Compare the results
    for key, val in defaultInputs.items():
        print(str(key) + ": " + str(val))
    assert my_dict == defaultInputs


if __name__ == '__main__':
    #filter_dict()
    #accidentally_create_a_set()
    list_to_dictionary()
    #combine_dictionaries()
