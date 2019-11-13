import random


def random_float():
    """ Generate a float in the range [0.0, 1.0) """
    for _ in range(10):
        print(random.random())


def random_integer():
    """ Range is inclusive of lower and upper bound """
    print(random.randint(0, 100))


def random_list_item():
    my_list = ["A", "list", "of", "values"]
    print(random.choice(my_list))


if __name__ == "__main__":
    random_float()
    #random_integer()
    #random_list_item()