#!/bin/python3

import os

#
# Complete the 'fibonacciModified' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER t1
#  2. INTEGER t2
#  3. INTEGER n
#


def fibonacciModified(t1, t2, n):
    if n == 1:
        return t1
    elif n == 2:
        return t2
    a = t1
    b = t2
    for _ in range(3, n + 1):
        next_step = b**2 + a

        a = b
        b = next_step

    return b


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    t1 = int(first_multiple_input[0])

    t2 = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    result = fibonacciModified(t1, t2, n)

    fptr.write(str(result) + "\n")

    fptr.close()
