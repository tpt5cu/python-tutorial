import os


def resolve_path_when_dirname_is_dot():
    '''
    Python can resolve a relative path just fine when the dirname is an empty string
    - It it appears that it cannot, it's because the code used os.chdir() somewhere so the relative path points to the completely wrong place
    '''
    print('os.path.dirname(__file__): ' + '~' + os.path.dirname(__file__) + '~') # empty string
    csv_path = os.path.join(os.path.dirname(__file__), '../../csv_/my-csv.csv')
    print(csv_path) # ../../csv_/my-csv.csv
    with open(csv_path) as f:
        text = f.read()
    print(text)


if __name__ == '__main__':
    resolve_path_when_dirname_is_dot()