import random


def randomize_sequence():
    '''random.shuffle modifies a sequence in place, so it cannot accept an iterator because it doesn't consumer the iterator'''
    #iter_ = range(10) # TypeError
    iter_ = list(range(10))
    random.shuffle(iter_)
    print(iter_) # [2, 5, 0, 9, 3, 1, 7, 8, 4, 6]


if __name__ == '__main__':
    randomize_sequence()