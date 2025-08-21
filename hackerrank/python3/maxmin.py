#!/bin/python3


#
# Complete the 'maxMin' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER k
#  2. INTEGER_ARRAY arr
#


def maxMin(k, arr):
    arr.sort()
    unfairness = arr[k - 1] - arr[0]

    for i in range(1, len(arr) - k + 1):
        t_unfairness = arr[i + k - 1] - arr[i]
        if t_unfairness < unfairness:
            unfairness = t_unfairness
    return unfairness


if __name__ == "__main__":
    n = int(input().strip())

    k = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = maxMin(k, arr)
