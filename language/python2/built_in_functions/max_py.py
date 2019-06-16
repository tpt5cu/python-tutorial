

def max_of_multidimensional():
    """ max() does not work out-of-the-box on multidimensional iterables """
    numbers = [
        [1, 1, 3, 1, 1],
        [999.9],
        [5, 1, 5, 1, 6],
        [7, 6, 1000.001],
        [-1, 0, 0, 0, 1, 0]
    ]
    #print(max(numbers)) # [999.9]
    # This is not what I want. max() is called on each list to compare each entire list to another list
    #print(reduce(max, numbers)) # [999.9]
    # Using reduce() won't work because reduce() will always return a list
    max_val = numbers[0][0]
    max_list_idx = 0
    max_inner_idx = 0
    for i in range(len(numbers)):
        for j in range(len(numbers[i])):
            if numbers[i][j] > max_val:
                max_val = numbers[i][j]
                max_list_idx = i
                max_inner_idx = j
    print("{}, {}, {}".format(max_val, max_list_idx, max_inner_idx)) # 1000.001, 3, 2


if __name__ == "__main__":
    max_of_multidimensional()