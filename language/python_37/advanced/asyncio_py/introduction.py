# https://realpython.com/async-io-python/


import asyncio, time


'''
- The asyncio package was introduced in Python 3.4
    - Thus it is possible to see the outdated "@asyncio.coroutine" decorator
        - Generator-based coroutines will be removed in Python 3.10
- The async/await syntax was introduced in Python 3.5
- There is no such thing as an async lambda. Also, lambdas are NEVER supposed to be named. Any time that I want a named function, I should always use
  a def statement
- In order to await an object, it must be awaitable. An object is awaitable if either is True:
    - It is a coroutine (i.e. a coroutine function or an asynchronous generator)
    - It defines an __await__() method that returns an iterator
'''

async def greet():
    print('Hello!')
    await asyncio.sleep(1.0)
    print('Goodbye!')


async def give_multiple_greetings():
    '''
    Hello!
    Hello!
    Hello!
    Goodbye!
    Goodbye!
    Goodbye!
    '''
    await asyncio.gather(greet(), greet(), greet())


def count():
    print('One')
    time.sleep(1.0)
    print('Two')


def count_three_times():
    '''
    One
    Two
    One
    Two
    One
    Two
    '''
    for _ in range(3):
        count()


if __name__ == '__main__':
    asyncio.run(give_multiple_greetings())
    count_three_times()