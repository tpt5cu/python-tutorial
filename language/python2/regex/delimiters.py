# https://docs.python.org/2/library/re.html
# https://stackoverflow.com/questions/3995034/do-python-regular-expressions-from-the-re-module-support-word-boundaries-b


import re


def word_boundary():
    """
    I want to find a word by itself. The word shouldn't be a substring of any other word.
    - The \b character class matches the boundary between a \w (alphanumeric character, which includes underscore) and \W (nonalphanumeric character)
        - This would include newlines, whitespace, etc.
    """
    string = "foo\nbar 1\nfoobar\nbazbarfoo\nfoo_bar\nfoo-bar-baz2\n'bar'3\nbar5"
    # This matches any instance of 'bar' that is a separate word. The reason this pattern does not match the entire string is because '.' matches
    # every character EXCEPT for the newline
    #matches = re.findall(r'.*\bbar\b.*', string) # Alternative syntax without a pattern object
    pattern = re.compile(r'.*\bbar\b.*')
    matches = pattern.findall(string)
    print(matches) # ['bar 1', 'foo-bar-baz2', "'bar'3"]
    mo = pattern.search(string)
    #mo = re.search(r'.*\bbar\b.*', string)
    print(mo.group()) # bar 1


if __name__ == "__main__":
    word_boundary()