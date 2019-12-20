import pathlib, itertools, math
from re_.complex_tasks.validate_open_modes import ensure_one_base_mode, alternate_ensure_one_base_mode


def get_permutations(base_mode):
    '''
    - ['r+b', 'rb+', '+rb', '+br', 'br+', 'b+r', 'r+t', 'rt+', '+rt', '+tr', 'tr+', 't+r', 'rb', 'br', 'rt', 'tr', 'r+', '+r', 'r']
    '''
    distinct_sets = [base_mode + suffix for suffix in ['+b', '+t', 'b', 't', '+', '']] 
    permutations = []
    for s in distinct_sets:
        permutations.extend([''.join(x) for x in itertools.permutations(s)])
    #print(permutations)
    return permutations


def get_all_permutations():
    all_permutations = []
    for base_mode in 'rwax':
        all_permutations.extend(get_permutations(base_mode))
    assert len(all_permutations) == 76
    return all_permutations


def _test_normal_permutations(permutations):
    '''This test harness shows that all permutations of a valid combination of characters are valid'''
    path = (pathlib.Path(__file__).parent / 'test.txt').resolve()
    for p in permutations:
        #print(p)
        with open(path, p):
            pass


def _test_exclusive_creation_permutations(permutations):
    path = (pathlib.Path(__file__).parent / 'new-test.txt').resolve()
    for p in permutations:
        #print(p)
        with open(path, p):
            pass
        path.unlink()


def test_all_permutations():
    p1 = get_permutations('r')
    p2 = get_permutations('w')
    p3 = get_permutations('a')
    p4 = get_permutations('x')
    for p in [p1, p2, p3]:
        _test_normal_permutations(p)
    _test_exclusive_creation_permutations(p4)
    all_permutations = [*p1, *p2, *p3, *p4]
    print(len(all_permutations)) # 76
    #print(all_permutations)
    #alternate_ensure_one_base_mode(all_permutations)
    #ensure_one_base_mode(all_permutations)


def view_readonly_modes():
    '''rb, br, rt, tr, r'''
    permutations = get_all_permutations()
    for p in permutations:
        if 'r' in p and '+' not in p:
            print(p)
        else:
            print('Write: {}'.format(p))


if __name__ == '__main__':
    #test_all_permutations()
    view_readonly_modes()