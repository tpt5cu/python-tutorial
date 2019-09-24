# Given a string, reverse the order of the vowels in the  string. Example: the cat jumped over the lazy dog = tho cyt jamped evor the luza deg

def reverse_vowels(string):
    """
    Use two pointers that scan the array from outside in, switching vowels as they are found. Terminate when the pointers point to the same index
    """
    if len(string) == 0:
        return ""
    ary = list(string)
    for i in range(0, len(ary), 1):
        j = len(ary) - 1 - i
        if i == j:
            break

    return str(ary))



if __name__ == '__main__':
    string = reverse_vowels('the cat jumped over the lazy dog')
    #assert string == 'tho cyt jamped evor the luza deg'