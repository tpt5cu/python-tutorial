# Find all palindromes in a string
# - A palindrome reads the same forwards and backwards.
# - 1 letter words are not palindromes
# - Instead of using a dict(), use an array. How do I get ascii integer values from character in Python? Use ord() and chr()


import re


"""
There has to be a way to do this in one actual pass, but I bet it's super annoying
1) pseudo code
2) write test cases
3) work through test cases and revise code as I go
4) profit
"""


def str_to_int():
    """Don't use the int() function to convert between strings and integers"""
    #a_val = int('a') # Bad
    a_val = ord('a')
    print(a_val) # 97
    a_val = ord('A')
    print(a_val) # 65
    print(chr(65)) # A


def sparse_list():
    """Out of the box, Python lists cannot be sparse. Use repetition to expand the list to the proper size first"""
    #my_list = []
    my_list = [0] * 26
    my_list[25] = 'z'
    print(len(my_list)) # 26
    print(my_list[25]) # z
    

def find_all_palindromes(sentence):    
    """
    This solution does a lot of work:
    - Generate an entire new immutable str that is in lowercase (O(n))
    - Generate more immutable substrings when the original string is split (O(n))
    - Iterate over every character in a substring, presumably generating a new immutable str for each character
    - Iterate over a dictionary for each substring to count the letter occurances (O(n))
    """
    def detect_palindrome(string):
        if len(string) <= 1: # Don't care about empty strings or 1 letter strings
            return
        counts = {}
        for c in string:
            if counts.get(c) is None:
                counts[c] = 1
            else:
                counts[c] += 1
        odd_count = 0
        for v in counts.itervalues():
            if v % 2 != 0:
                odd_count += 1
        if odd_count < 2:
            return string
    sentence = sentence.lower() # Uppercase and lowercase letters are the same for the purposes of detecting a palindrome
    #words = sentence.split(' ') # The <str>.split() method only accepts a single delimiter so it can't handle punctuation adjacent to a palindrome
    words = filter(lambda w: len(w) > 1, re.split('\W', sentence))
    for w in words:
        result = detect_palindrome(w)
        if result is not None:
            print(result)


def find_all_palindromes_better(sentence):
    """
    - A = 65 and a = 97, so there is a difference of 32. 
    - I don't need a bytearray() to implement a bit vector
    """
    if len(sentence) < 2:
        return

    def int_val(b):
        return b - 65 if (b - 65 < 26 and b - 65 >= 0) else b - 97

    def is_alphanumeric(b):
        return int_val(b) < 26 and int_val(b) >= 0

    def detect_palindrome(ba, start, end):
        vector = 0
        for i in xrange(start, end + 1):
            vector ^= 1 << int_val(ba[i])
        if bin(vector).count('1') < 2:
            print(ba[start: end + 1])

    start, end = None, None
    ba = bytearray(sentence)
    for i in xrange(len(ba)):
        if end is None and is_alphanumeric(ba[i]) and start is None:
            start = i
        elif start is not None and is_alphanumeric(ba[i]):
            end = i
        elif (start is not None and end is not None) and (not is_alphanumeric(ba[i]) or i == len(ba) - 1):
            detect_palindrome(ba, start, end)
            start, end = None, None
        # I was actually so close when I wrote this on the whiteboard. I was just missing this last case to check for when I find a single
        # alphanumeric character while traversing the string!
        else:
            start, end = None, None



if __name__ == "__main__":
    sentence = 'Hello. I like Llama. My friend Hannah,     and racecar.' # 4 empty strings in sentence.split()
    #str_to_int()
    #sparse_list()
    find_all_palindromes(sentence)
    find_all_palindromes_better(sentence)