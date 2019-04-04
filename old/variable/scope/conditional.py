

def if_statement_scope(num):
    """A variable can be DECLARED inside of an if-statement (or for-loop, etc.) and it will be visible outside of the
    control structure. However, a variable cannot be USED anywhere before it has been declared. This is true anywhere,
    I just confounded the issue with control-structures.
    """
    if num > 5:
        """'var' has not been declared and assigned anywhere, so it cannot be used here. I can ASSIGN var inside of
        the if-statement no problem.
        """
        #var = 0
        var = var + 100
        var += 100
    print(var)


if __name__ == "__main__":
    if_statement_scope()