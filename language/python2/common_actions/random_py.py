import random


def random_integer():
    """ Range is inclusive of lower and upper bound """
    print(random.randint(0, 100))


def random_list_item():
    my_list = ["A", "list", "of", "values"]
    print(random.choice(my_list))


if __name__ == "__main__":
    random_integer()
    random_list_item()