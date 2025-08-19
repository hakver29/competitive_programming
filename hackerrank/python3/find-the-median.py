#!/bin/python3

import os

#
# Complete the 'findMedian' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def findMedian(arr):
    arr.sort()
    n = len(arr)
    if n % 2 == 0:
        return (arr[n // 2] + arr[n // 2 + 1]) / 2
    return arr[n // 2]
    # Write your code here


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = findMedian(arr)

    fptr.write(str(result) + "\n")

    fptr.close()
