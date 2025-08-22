#!/bin/python3


#
# Complete the 'maxSubarray' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY arr as parameter.
#


def maxSubarray(arr):
    n = len(arr)

    S1 = arr[0]
    maxEnding = arr[0]
    for i in range(1, n):
        maxEnding = max(maxEnding + arr[i], arr[i])

        S1 = max(S1, maxEnding)

    S2 = sum([x for x in arr if x > 0])

    return [S1, S2]

    # Write your code here


if __name__ == "__main__":
    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = maxSubarray(arr)
        print(result)
