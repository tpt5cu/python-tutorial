# https://docs.python.org/3/whatsnew/3.3.html
# https://utcc.utoronto.ca/~cks/space/blog/python/YieldFromAndGeneratorFunctions
# https://stackoverflow.com/questions/9708902/in-practice-what-are-the-main-uses-for-the-new-yield-from-syntax-in-python-3
# http://www.dabeaz.com/coroutines/


'''
The "yield from" statement is primarily for making it easier to chain multiple generators together and share state between them
- I honestly don't know enough to need to understand why "yield from" is so important right now
- Those slides on coroutines were insane!
'''


def get_individual_numbers():
    for i in range(10):
        yield i


def get_all_numbers():
    yield from range(10)


def consume_generators():
    # These lines are not what I want. Why? Because neither statement is consuming a generator
    print(get_individual_numbers()) # <generator object get_individual_numbers at ...>
    print(get_all_numbers()) # <generator object get_all_numbers at ...>
    #gen = get_individual_numbers()
    #gen = get_all_numbers()
    #try:
    #    while True:
    #        print(next(gen))
    #except StopIteration:
    #    pass



if __name__ == '__main__':
    consume_generators()