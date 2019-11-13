def concatenate_literal():
    '''Concatenation is intuitive'''
    ba = bytearray()
    ba += 'hello'
    ba += bytearray(' world')
    print(type(ba))
    print(ba)


if __name__ == '__main__':
    concatenate_literal()