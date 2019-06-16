"""
https://stackoverflow.com/questions/14050824/add-sum-of-values-of-two-lists-into-new-list
"""


def sum_two_lists():
    first = [1, 2, 3]
    second = [4, 5, 6]
    list_sum = [x + y for x, y in zip(first, second)]
    print(list_sum) # [5, 7, 9]


if __name__ == "__main__":
    sum_two_lists()