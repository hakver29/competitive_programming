#!/bin/python3

import os

#
# Complete the 'lilysHomework' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def calculate_swaps(arr, sorted_arr):
    arr_copy = arr[:]

    hashmap = {value: index for index, value in enumerate(arr_copy)}
    swaps = 0

    for i in range(len(arr_copy)):
        if arr_copy[i] != sorted_arr[i]:
            swaps += 1

            correct_val = sorted_arr[i]
            idx = hashmap[correct_val]
            val_to_swap = arr_copy[i]
            arr_copy[i], arr_copy[idx] = arr_copy[idx], arr_copy[i]

            hashmap[correct_val] = i
            hashmap[val_to_swap] = idx

    return swaps


def lilysHomework(arr):
    descending_swaps = calculate_swaps(arr, sorted(arr, reverse=False))
    ascending_swaps = calculate_swaps(arr, sorted(arr, reverse=True))

    return min(descending_swaps, ascending_swaps)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = lilysHomework(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
