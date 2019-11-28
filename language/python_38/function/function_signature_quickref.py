# https://stackoverflow.com/questions/24735311/python-what-does-the-slash-mean-in-help-output - position only parameters (i.e. "/" in the function
# signature) will only be available in Python 3.8 or 3.9
# https://stackoverflow.com/questions/14301967/bare-asterisk-in-function-arguments


def keyword_only_parameters(first, second, *, third):
    '''
    A bare asterisk in a function signature means that all subsequent arguments must be passed with keyword syntax
    - Just because an argument is keyword only doesn't mean it isn't required
    '''
    s = first + second
    if third:
        return s + third
    return s


if __name__ == '__main__':
    #print(keyword_only_parameters(5, 5)) # TypeError: missing required keyword-only argument
    #print(keyword_only_parameters(5, 5, 11)) # TypeError: 2 positional arguments expected but 3 were given
    print(keyword_only_parameters(5, 5, third=11)) # 21