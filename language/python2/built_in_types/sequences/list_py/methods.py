# https://docs.python.org/2.7/tutorial/datastructures.html - some of list's methods
# https://stackoverflow.com/questions/11520492/difference-between-del-remove-and-pop-on-lists


def append_py():
    """list.append() adds an element to the end of the list in-place."""
    my_list = [1, 2, 3]
    my_list.append(4)
    # append() only accepts a single argument
    #my_list.append(5, 6)
    my_list.append([5, 6])
    print(my_list) #[1, 2, 3, 4, [5, 6]] This is not what I want


def prepend():
    my_list = [4, 5, 6]
    my_list.insert(0, "X")
    print(my_list)


def extend_py():
    """
    extend() only takes 1 iterable argument, but the elements inside of that argument are appended to the list directly. This is an in-place
    modification!
    - The other sequence that is being used to extend the target list is unchanged
    """
    my_list = [1, 2, 3]
    other = [4, 5]
    my_list.extend(other)
    print(other) # [4, 5]
    print(my_list) #[1, 2, 3, 4, 5]
    my_list.extend(("cat", "dog", "bog"))
    print(my_list) # [1, 2, 3, 4, 5, 'cat', 'dog', 'bog']
    my_list.extend('hi')
    print(my_list) # [1, 2, 3, 4, 5, 'cat', 'dog', 'bog', 'h', 'i']


def remove_py():
    """
    remove() removes an item with the specified value. If the value doesn't exist in the list, it's an error
    - del removes an element by index
    - pop() removes an element by index and returns it
    - remove() removes an element by value
    """
    my_list = [1, 2, 3]
    my_list.remove(2)
    print(my_list) # [1, 3]
    #my_list.remove(66) # ValueError


def find_element():
    """If the element is not found in the list, Python made the design decision to raise an error. I should use the 'in' operator instead"""
    my_list = ['a', 'b', 'c', 'd']
    print(my_list.index('c')) # 2
    #print(my_list.index(1)) # ValueError


def shift():
    """Insertion and popping are in-place operations, so shifting is an in-place operation."""
    my_list = [1, 2, 3, 4, 5]
    my_list.insert(0, my_list.pop()) # Remove the last item, return it, then reinsert that item as the first item in the list
    print(my_list)


def count_py():
    """<list>.count() is very useful for assert statements. Apparently 1 == True?"""
    my_list = [True, False, False, True, 1, 2, 3, 4]
    print(my_list.count(True)) # 3. How about that!
    for x in my_list:
        print(str(x) + ". x == True: " + str(x == True))


def filter_py():
    """Use the built-in filter() function"""
    pass


def iterate_with_index():
    """Use the built-in enumerate() function"""
    pass


if __name__ == "__main__":
    #append_py()
    #prepend()
    extend_py()
    #remove_py()
    #find_element()
    #shift()
    #count_py()
    #filter_py()