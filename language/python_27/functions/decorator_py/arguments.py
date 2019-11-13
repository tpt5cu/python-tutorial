# https://stackoverflow.com/questions/36901/what-does-double-star-asterisk-and-star-asterisk-do-for-parameters


def excellent_decorator(func):
    def wrapper(*args, **kwargs):
        """
        Here, args (a tuple) and kwargs (a dict) only contain those arguments that were passed in by the invoking context. If the invoking context
        didn't pass any arguments WITH THE KEYWORD ARGUMENT SYNTAX, then kwargs will be empty.
        - E.g. if an argument was passed for the "activity" parameter, but the argument didn't use the "=" syntax, then the arguement for the
          "activity" parameter will only exist in the args tuple.
        - E.g. If an argument was passed for the "activity" parameter with the keyword argument syntax, then that argument will only exist in kwargs
          and not in args
        """
        print("wrapper did stuff")
        """
        At this point in the stack, *args is not a variable, but args is. **kwargs is not a variable, but kwargs is. Since that is the case, how do I
        pass these nonexistent variables into the function as arguments? This syntax works, so how are *args and **kwargs turned into valid arguments?

        It turns out that args and kwargs can be used (i.e. unpacked) when calling a function as well. It's very special syntax.
        """
        return func(*args, **kwargs)
    return wrapper


@excellent_decorator
def say_my_name(name, color, activity="bopping"):
    """args and kwargs don't exist here, since they weren't declared as parameters"""
    print("My name is {} and I am {} and I like {}.".format(name, color, activity))


def count_to_three(one, two, three):
    print(one)
    print(two)
    print(three)


def unpack_args_when_calling():
    """Apparently a list can only be unpacked inside the parentheses of an invoking function. Tricky!"""
    my_list = [1, 2, 3]
    #count_to_three(my_list) # TypeError
    #x = *my_list # SyntaxError
    count_to_three(*my_list) # Works great!


def unpack_kwargs_when_calling():
    """
    If I use special syntax to unpack a dictionary into a function that I'm invoking, the keys of the dictionary must exactly match the parameters of
    the function being invoked. It turns out that Flask doesn't provide this behavior, Python does!
    """
    my_dict = {"one": 1, "two": 2, "three": 3}
    #my_dict = {"one": 1, "two": 2, "thre": 3} # TypeError
    #count_to_three(my_dict) # TypeError
    #x = **my_dict # Invalid syntax
    count_to_three(**my_dict) # Works great!



if __name__ == "__main__":
    """
    I already know that the decorator function takes another function as an argument and returns a new function. "say_my_name" is thus really the
    wrapper function.
    """
    #say_my_name("Bob", "turquoise", activity="jumping")
    #unpack_args_when_calling()
    unpack_kwargs_when_calling()