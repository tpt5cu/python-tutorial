import a


def say_hello_from_b():
    print('Hello from b.py')


if __name__ == '__main__':
    print('__main__ is b.py')
    say_hello_from_b()
    a.say_hello_from_a()