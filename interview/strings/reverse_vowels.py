# Given a string, reverse the order of the vowels in the  string. Example: the cat jumped over the lazy dog = tho cyt jamped evor the luza deg


def reverse_vowels(string):
    """
    Use two pointers that scan the array from outside in, switching vowels as they are found. Terminate when the pointers point to the same index
    - This isn't a hard problem, but I need to take my time!
    """
    if len(string) <= 1:
        return string
    ary = list(string)
    vowels = {'a': 'a', 'e': 'e', 'i': 'i', 'o': 'o', 'u': 'u', 'y': 'y'} # I forgot to include 'y' as a vowel! Take my time!
    i = 0
    j = len(string) - 1
    while i < j: # I originally used a double for-loop! Take my time!
        count = 0
        if vowels.get(ary[i].lower()) is not None:
            count += 1
        else:
            i += 1
        if vowels.get(ary[j].lower()) is not None: # I originally didn't decrement j all the time. Take my time!
            count += 1
        else:
            j -= 1
        if count == 2:
            swap(ary, i, j)
            i += 1
            j -= 1
    return ''.join(ary)


def swap(ary, i , j):
    temp = ary[i]
    ary[i] = ary[j]
    ary[j] = temp


if __name__ == '__main__':
    string = reverse_vowels('the cat jumped over the lazy dog')
    print(string)
    assert string == 'tho cyt jamped evor the luza deg'