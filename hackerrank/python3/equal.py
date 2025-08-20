#!/bin/python3

#
# Complete the 'equal' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY arr as parameter.
#
import os


def equal(arr):
    arr.sort()
    min_ops = float("inf")

    for target_offset in range(5):
        current_target = arr[0] - target_offset
        total_current_ops = 0

        for x in arr:
            diff = x - current_target

            ops_for_element = 0
            ops_for_element += diff // 5
            diff = diff % 5

            ops_for_element += diff // 2
            diff = diff % 2

            ops_for_element += diff

            total_current_ops += ops_for_element

        min_ops = min(min_ops, total_current_ops)
    return min_ops


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = equal(arr)

        fptr.write(str(result) + "\n")

    fptr.close()
