"""
The "*<whatever>" (commonly "*args") parameter is used to pass a tuple argument to a function, where the tuple is constructed from the arguments that
are passed to the function.
"""


def print_foods(name, *foods):
    for food in foods:
        print("My name is {name}, and I like to eat {food}".format(name=name, food=food))
    my_list = ["yay"]
    print(type(my_list))
    print(type(foods))


""" If *args is used, it must be the LAST argument """
#def invalid_syntax(*pets, owner):
def invalid_syntax(owner, *pets):
    print("Mr.{owner} owns {pets}".format(owner=owner, pets=str(pets)))


if __name__ == "__main__":
    #print_foods("rice", "beans", "nectarine", "dog food")
    invalid_syntax("Austin", "cat", "dog", "fish", "frog")