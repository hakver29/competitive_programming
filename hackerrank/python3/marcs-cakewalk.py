#!/bin/python3

import heapq
import os

#
# Complete the 'marcsCakewalk' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts INTEGER_ARRAY calorie as parameter.
#


def marcsCakewalk(calorie):
    max_heap = [-c for c in calorie]
    heapq.heapify(max_heap)
    total_miles = 0
    for i in range(len(calorie)):
        largest = -heapq.heappop(max_heap)
        total_miles += 2**i * largest
    return total_miles


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    n = int(input().strip())

    calorie = list(map(int, input().rstrip().split()))

    result = marcsCakewalk(calorie)

    fptr.write(str(result) + "\n")

    fptr.close()
