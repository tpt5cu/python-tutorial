import numpy as np


def random_choice_consumer_generator():
    '''
    Both the array and probabilities can be generators
    - It's safe to assume that the rest of the functions in np.random also will consumer generators
    - However, a dict_keys object is NOT accepted, regardless of what the keys are
    '''
    # All of the following cause: ValueError: a must be 1-dimensional or an integer
    #list_like = {'foo': 'bar', 'baz': 'boo'}.keys()
    #list_like = {'8': 'bar', '10': 'boo'}.keys()
    #list_like = {1: 'bar', 2: 'boo'}.keys()

    # All of the following work. It doesn't matter what the keys are
    list_like = range(1, 5)
    #list_like = list({'foo': 'bar', 'baz': 'boo'}.keys())
    #list_like = list({'8': 'bar', '10': 'boo'}.keys())
    #list_like = list({1: 'bar', 2: 'boo'}.keys())

    print(np.random.choice(list_like))


if __name__ == '__main__':
    random_choice_consumer_generator()