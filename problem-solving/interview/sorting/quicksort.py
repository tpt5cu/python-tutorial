# https://stackoverflow.com/questions/10425506/intuitive-explanation-for-why-quicksort-is-n-log-n


"""
- Low and high indexes are inclusive to make my life easier
- I made 3 mistakes:
    - Don't include the partition index in the next recursive call
    - Quicksort only happens if low < high
    - ltz is NOT -1. It's simple 1 less than the low index

Ideal runtime: O(n * log(n))
    - Each partition step takes O(n) to pass over all of the elements in the array
    - There are log_2(n) instances of partitioning that occur, assuming that the input is divided in half each time
        - E.g log_2(128) = 7 becuase 128 -> 64 -> 32 -> 16 -> 8 -> 4 -> 2 -> 1

Worst case runtime: O(n^2)
    - Each partition step takes O(n)
    - If the pivot is the smallest (or largest, depending on the implementation) value, then each level of partitioning will only reduce the size of
    the larger partition by 1. n * n - 1 is O(n^2)
"""


def quicksort(ary, low, high):
    if (low < high):
        p = partition(ary, low, high)
        #quicksort(ary, low, p)
        # Mistake! Only perform quicksort at ALL if low < high
        # Mistake! Don't include the partition index in any more recursive calls because it causes infinite recursion. Everything is already sorted
        # around the partition so I don't need to include it
        quicksort(ary, low, p - 1)
        quicksort(ary, p + 1, high)


def partition(ary, low, high):
    pivot = ary[high]
    # Mistak! ltz always = -1 is not correct when I'm sorting the right-hand side. This caused infinite recursion
    ltz = low - 1 # ltz == less than zone
    for i in range(low, high + 1):
        if ary[i] <= pivot:
            ltz += 1
            swap(ary, ltz, i)
    return ltz


def swap(ary, ltz, i):
    t = ary[ltz]
    ary[ltz] = ary[i]
    ary[i] = t


if __name__ == '__main__':
    ary = [6, 3, 9, 2, 8, 5, 5]
    quicksort(ary, 0, len(ary) - 1) # [2, 3, 5, 5, 6, 8, 9]
    print(ary)
    ary = [10, 9, 8, 7, 6, 5]
    quicksort(ary, 0, len(ary) - 1) # [5, 6, 7, 8, 9, 10]
    print(ary)
    ary = [5, 5, 5, 4, 5, 5, 5]
    quicksort(ary, 0, len(ary) - 1) # [4, 5, 5, 5, 5, 5, 5]
    print(ary)
