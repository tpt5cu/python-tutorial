# Find all palindromes in a string
# - A palindrome reads the same forwards and backwards.
# - Instead of using a dict(), use an array. How do I get ascii integer values from character in Python? Use ord() and chr()


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
    

def detect_palindrome(string):    
    





if __name__ == "__main__":
    #str_to_int()
    sparse_list()