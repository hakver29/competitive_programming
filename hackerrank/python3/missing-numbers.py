#!/bin/python3


#
# Complete the 'missingNumbers' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY arr
#  2. INTEGER_ARRAY brr
#


def missingNumbers(arr, brr):
    arr.sort()
    brr.sort()

    missing = []

    while brr:
        val = brr.pop(
            0
        )  # pop(0) is slow, that's why the second implementation is better
        if arr and arr[0] == val:
            arr.pop(0)
        else:
            missing.append(val)

    missing = sorted(list(set(missing)))

    return missing


def missingNumbers2(arr, brr):
    arr.sort()
    brr.sort()

    missing = []
    i = 0
    j = 0
    while j < len(brr):
        if i < len(arr) and arr[i] == brr[j]:
            i += 1
            j += 1
        else:
            missing.append(brr[j])
            j += 1
    unique_missing = sorted(list(set(missing)))
    return unique_missing


if __name__ == "__main__":
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    m = int(input().strip())

    brr = list(map(int, input().rstrip().split()))

    result = missingNumbers(arr, brr)

    print(result)
