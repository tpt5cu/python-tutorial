def if_statement(boolean):
    """
    Python variable scoping is very weird. If the if-statement evaluates, then the variable will be assigned and everything will work fine. If the
    if-statement does not evaluate, then the variable is NOT assigned an an Exception will be raised. The compiler does not protect me from possibly
    referencing an undeclared variable, probably because Python isn't technically compiled. If it works, it works. If it doesn't, it's my fault
    anyway!
    
    I assume this is also True for for-loops and other blocks.
    """
    if boolean is True:
        color = "red"
    print(color)


if __name__ == "__main__":
    # This works fine
    #if_statement(True)
    # UnboundLocalError
    if_statement(False)