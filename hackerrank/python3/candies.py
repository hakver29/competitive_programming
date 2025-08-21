#!/bin/python3


#
# Complete the 'candies' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER_ARRAY arr
#


def candies(n, arr):
    candies = [0] * n
    candies[0] = 1
    for i in range(1, n):
        if arr[i] - arr[i - 1] > 0:
            candies[i] = candies[i - 1] + 1
        else:
            candies[i] = 1
    for i in range(n - 2, -1, -1):
        if arr[i] > arr[i + 1] and candies[i] <= candies[i + 1]:
            candies[i] = max(candies[i], candies[i + 1]) + 1
    return sum(candies)


if __name__ == "__main__":
    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr_item = int(input().strip())
        arr.append(arr_item)

    result = candies(n, arr)
    print(result)
