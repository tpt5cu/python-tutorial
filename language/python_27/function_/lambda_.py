# https://treyhunner.com/2018/09/stop-writing-lambda-expressions/
# https://www.programiz.com/python-programming/anonymous-function


'''
An anonymous function is also known as a lambda function in many programming languages. Python is no different. A lambda returns the result of its
expression. One unique thing about Python lambdas is that they can have exactly 1 line of code. Syntax: lambda <args>: expression

Note that all functions in Python can be passed around, so sometimes I don't even need to use a lambda
'''


def no_argument_lambda():
    


def filter_lambda():
    '''filter() returns elements for whom the function argument returns true'''
    my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    even_list = filter(lambda x: x % 2 == 0, my_list)
    odd_list = filter(lambda x: x % 2 == 1, my_list)
    print(my_list)
    print(even_list)
    print(odd_list)


def extraction_lambda():
    '''The built-in sorted() function works on numbers perfectly fine with only 1 argument (the iterable).'''
    #my_list = [6, 523, -5, -8, 0, 32, -34, 7, -89, 3, -2]
    #sorted_list = sorted(my_list)
    #print(sorted_list)
    class container(object):

        def __init__(self, num):
            self.num = num
        
        def __repr__(self):
            return 'I contain: ' + str(self.num)

    containers = []
    containers.append(container(3))
    containers.append(container(1))
    containers.append(container(2))
    print(containers)
    # This won't work because abs() expects a number argument, not a container argument
    #print(sorted(containers, key=abs))
    print(sorted(containers, key=lambda c: c.num))


if __name__ == '__main__':
    #filter_lambda()
    extraction_lambda()