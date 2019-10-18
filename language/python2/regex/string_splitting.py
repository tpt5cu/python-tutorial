import re


def split_punctuation_and_whitespace():
    """
    Remember that just like with <str>.split(), if adjacent delimiters are found in the string, then an empty string is returned in the list
    - Raw strings simply mean that Python won't perform additional interpreting of the string literals before they are passed to the regex engine
    - The \W character class matches any non-alphanumeric character, i.e. [^a-zA-Z0-9_]
    - The '.' character matches any character
    - Use the or '|' symbol to match different possible patterns. Don't use capture groups for this purpose!
    """
    sentence = 'Hello. I like Llamas. My friend Hannah,     and racecars.'
    words = re.split(r'\W', sentence) 
    print(words) # ['Hello', '', 'I', 'like', 'Llamas', '', 'My', 'friend', 'Hannah', '', '', '', '', '', 'and', 'racecars', '']
    words = filter(lambda w: len(w) > 1, re.split(r'\W', sentence))
    print(words) # ['Hello', 'like', 'Llamas', 'My', 'friend', 'Hannah', 'and', 'racecars']
    words = re.split(r'\.|,|\s', sentence)
    print(words) # ['Hello', '', 'I', 'like', 'Llamas', '', 'My', 'friend', 'Hannah', '', '', '', '', '', 'and', 'racecars', '']
    words = filter(lambda w: len(w) > 1, re.split(r'\.|,|\s', sentence))
    print(words) # ['Hello', 'like', 'Llamas', 'My', 'friend', 'Hannah', 'and', 'racecars']
    # Using \W+ or \W* is even better than \W, but if there's a delimiter at the end of the string, an empty string will be included in the returned
    # list because the ending delimiter has no alphanumeric character on its right side, so it's treated as 2 adjacent delimiters.
    words = re.split(r'\W*', sentence) # ['Hello', 'I', 'like', 'Llamas', 'My', 'friend', 'Hannah', 'and', 'racecars', '']
    print(words)


if __name__ == '__main__':
    split_punctuation_and_whitespace()