def if_statement(boolean):
    '''
    Python variable scoping is very weird. If the if-statement evaluates, then the variable will be assigned and everything will work fine. If the
    if-statement does not evaluate, then the variable is NOT assigned an an Exception will be raised. The compiler does not protect me from possibly
    referencing an undeclared variable, probably because Python isn't technically compiled. If it works, it works. If it doesn't, it's my fault
    anyway!
    '''
    if boolean is True:
        color = "red"
    print(color)


def for_loop(var):
    '''Surprise! If a for-loop variable shadows a local variable, that local variable will be lost!'''
    print(var) # pie
    for var in [1, 2, 3]:
        print(var) # 1 2 3
    print(var) # 3


if __name__ == "__main__":
    # This works fine
    #if_statement(True)
    #if_statement(False) # UnboundLocalError
    for_loop('pie')