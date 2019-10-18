# Reverse every word in a sentence, but don't reverse the order of words in the sentence. Actually no. That's easy
# Reverse the order of the words in a sentence, but don't reverse the individual words themselves


def easy_reverse_words(sentence):
    return ' '.join(reversed(sentence.split(' '))) # Almost but not quite


"""I could implement the 'complicated' version very similarly to find_all_palindromes"""


if __name__ == '__main__':
    sentence = 'I like potatoes and apple juice.'
    rs = easy_reverse_words(sentence)
    print(type(rs))
    print(rs)