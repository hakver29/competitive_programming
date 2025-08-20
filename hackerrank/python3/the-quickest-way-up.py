#!/bin/python3

import os
from collections import deque

#
# Complete the 'quickestWayUp' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. 2D_INTEGER_ARRAY ladders
#  2. 2D_INTEGER_ARRAY snakes
#


def quickestWayUp(ladders, snakes):
    start_node = 1
    queue = deque([start_node])
    distances = [-1] * 101
    distances[start_node] = 0

    ladders_map = {ladder[0]: ladder[1] for ladder in ladders}
    snakes_map = {snake[0]: snake[1] for snake in snakes}

    while queue:
        current = queue.popleft()
        if current == 100:
            break
        for i in range(1, 7):
            final = current + i
            if final > 100:
                continue
            if final in snakes_map:
                final = snakes_map[final]
            elif final in ladders_map:
                final = ladders_map[final]
            if distances[final] == -1:
                distances[final] = distances[current] + 1
                queue.append(final)
    return distances[100]


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        ladders = []

        for _ in range(n):
            ladders.append(list(map(int, input().rstrip().split())))

        m = int(input().strip())

        snakes = []

        for _ in range(m):
            snakes.append(list(map(int, input().rstrip().split())))

        result = quickestWayUp(ladders, snakes)

        fptr.write(str(result) + "\n")

    fptr.close()
