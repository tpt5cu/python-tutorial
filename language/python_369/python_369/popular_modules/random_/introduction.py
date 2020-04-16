# https://docs.python.org/3.6/library/random.html


import random


def randomize_sequence():
    '''random.shuffle modifies a sequence in place, so it cannot accept an iterator because it doesn't consumer the iterator'''
    #iter_ = range(10) # TypeError
    iter_ = list(range(10))
    random.shuffle(iter_)
    print(iter_) # [2, 5, 0, 9, 3, 1, 7, 8, 4, 6]


def random_choice():
    '''random.choice() subscripts the sequence, so it cannot accept a generator'''
    dict_ = { 'foo': 1, 'bar': 2 }
    #print(random.choice(dict_.values())) # TypeError
    print(random.choice(list(dict_.values())))


def random_int():
    '''
    random.randrange(<start>, <stop>, <step>)
    - <stop> is an excluded upper bound
    - random.randint() is an alias for random.randrange()
    '''
    for _ in range(3):
        print(random.randrange(0, 10, 2)) # 2 6 4


if __name__ == '__main__':
    #randomize_sequence()
    #random_choice()
    random_int()
