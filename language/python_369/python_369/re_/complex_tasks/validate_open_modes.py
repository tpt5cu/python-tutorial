# https://stackoverflow.com/questions/247167/exclusive-or-in-regular-expression - regex XOR
# https://stackoverflow.com/questions/6617533/regex-unordered-matches - just use a HashSet


import re


'''
It sadly turns out that what I'm trying to do is not easy with regex. 
- Exclusive OR is hard
- Unordered match is hard

1. It must contain exactly one of r, a, w, or x (XOR)
2. It can contain either t or b or neither (Optional and XOR)
3. It can contain + or not (Optional)
4. Order does not matter (Unordered
'''


def ensure_one_base_mode(permutations):
    # This just doesn't work
    for p in permutations:
        if not re.search(r'(?<![rwax])[rwax](?=![rwax])', p):
            print('Error: {}'.format(p))


def alternate_ensure_one_base_mode(permutations):
    '''Insted of trying to use a regex to do everything, I can also count how many times a pattern was matched'''
    for p in permutations:
        matches = re.findall(r'[rwax]', p)
        if len(matches) == 0 or len(matches) > 1:
            print('Error: {}'.format(p))
