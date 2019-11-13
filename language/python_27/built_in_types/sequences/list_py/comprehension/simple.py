# https://stackoverflow.com/questions/4081217/how-to-modify-list-entries-during-for-loop
# https://www.programiz.com/python-programming/list-comprehension
# https://docs.python.org/3/tutorial/datastructures.html
# https://stackoverflow.com/questions/30245397/why-is-a-list-comprehension-so-much-faster-than-appending-to-a-list
# https://stackoverflow.com/questions/6475314/python-for-in-loop-preceded-by-a-variable


"""A list comprehension is an elegant way to create a new list based on an existing list."""


def basic_list_comprehension():
    """ 
    The syntax is: [<expression> for <item> in <iterable>].
    It could also be restated as: [<Do this to the item and return the result to a new list> for <item> in <iterable>].
    """
    # Get the individual letters (which are strings) of a string
    letters = [c for c in 'humans']
    print(type(letters))
    print(letters)


def comprehension_and_declaration():
    """Sometimes I don't want to have to declare a list separately. I want to declare and use a comprehension simultaneously"""
    # This works. It must be iterating over a tuple
    red_pets = ['red ' + pet for pet in 'cat', 'dog', 'fish', 'bird']
    print(red_pets)
    # This also works. It is iterating over the list
    blue_pets = ['blue ' + pet for pet in ['ferret', 'rhino', 'dragon', 'elphant']]
    print(blue_pets)


def add_a_value():
    """
    Since modifying a list during iteration is poor form, a list comprehension can apply the change (i.e. expression)
    to every element and put the result in a new list (this is called mapping!)
    """
    numbers = [1, 2, 3, 4, 5]
    more_numbers = [num + 5 for num in numbers]
    print(more_numbers)


def sum_numbers():
    """It turns out a list comprehension is NOT suited to this problem, or to every problem."""
    # The desired output is [4, 11, 20, 30, 85], aka the sum of all numbers up to that point.
    numbers = [4, 7, 9, 10, 55]
    # This prints the total sum, but not the sum up to each point.
    print(sum(numbers))
    # This won't work because even though it IS summing subsequent numbers, it isn't using the previous sum in 
    # the current sum, because all 'vals' are coming from the original list.
    #sum_of_list = [val + numbers[idx - 1] for idx, val in enumerate(numbers) if idx > 0]
    #This works, but it's horrible.
    list_sum = []
    for idx, val in enumerate(numbers):
        if idx > 0:
            s = numbers[idx] + list_sum[idx - 1]
            list_sum.append(s)
        else:
            list_sum.append(numbers[idx])
    print(list_sum)

if __name__ == "__main__":
    #basic_list_comprehension()
    comprehension_and_declaration()
    #add_a_value()
    #sum_numbers()
