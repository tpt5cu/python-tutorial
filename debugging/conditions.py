# https://www.jetbrains.com/help/pycharm/configuring-breakpoints.html


def equals_loop():
    """I set the condition for this breakpoint to be x==6. That means the breakpoint should only activate when x==6.
    """
    for x in range(10):
        x += 1
        print(x)


def greater_than_loop():
    """I set the condition for this breakpoint to be x > 90."""
    for x in range(100):
        print(x)


def string_contains():
    """Any valid python expression that evaluates to True or False can be used as a condition. I use the 'in' operator
    to check if a substring exists with the larger string as the condition. Also note that the breakpoint doesn't
    need to be on the same line as the variable I'm investigating.
    """
    string = "AAA"
    for x in range(100):
        if x == 77:
            string = string[:1] + "B" + string[2:]
        print(x)
    print(string)


if __name__ == "__main__":
    #equals_loop()
    #greater_than_loop()
    string_contains()
