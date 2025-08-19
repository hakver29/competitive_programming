#!/bin/python3

import os


def flatlandSpaceStations(n, c):
    if n == len(c):
        return 0

    dist = -float("inf")
    for i in range(n):
        d = float("inf")
        for j in c:
            if abs(j - i) < d:
                d = abs(j - i)
            if d <= dist:
                break

        if d > dist:
            dist = d
    return dist


def flatlandSpaceStations2(n, c):
    c.sort()

    max_dist = max(c[0], (n - 1) - c[-1])

    for i in range(1, len(c)):
        distance_between_space_stations = c[i] - c[i - 1]
        max_dist = max(max_dist, distance_between_space_stations // 2)

    return max_dist


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + "\n")

    fptr.close()
