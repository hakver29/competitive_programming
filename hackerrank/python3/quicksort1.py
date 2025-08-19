#!/bin/python3

import os

#
# Complete the 'quickSort' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def quickSort(arr):
    pivot = arr[0]
    lte = [x for x in arr[1:] if x <= pivot]
    gte = [x for x in arr[1:] if x > pivot]
    return lte + pivot + gte


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = quickSort(arr)

    fptr.write(" ".join(map(str, result)))
    fptr.write("\n")

    fptr.close()
