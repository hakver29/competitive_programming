#!/bin/python3

import os

#
# Complete the 'bfs' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER m
#  3. 2D_INTEGER_ARRAY edges
#  4. INTEGER s
#
from collections import deque


def bfs(n, m, edges, s):
    start_node = s - 1
    queue = deque([start_node])
    distances = [-1 for i in range(n)]
    distances[start_node] = 0

    adj_list = [[] for _ in range(n)]
    for u, v in edges:
        u_idx = u - 1
        v_idx = v - 1
        adj_list[u_idx].append(v_idx)
        adj_list[v_idx].append(u_idx)

    while queue:
        current = queue.popleft()
        for v in adj_list[current]:
            if distances[v] == -1:
                distances[v] = distances[current] + 6
                queue.append(v)
    result = []
    for i in range(n):
        if i != start_node:
            result.append(distances[i])
    return result

    # Write your code here


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        edges = []

        for _ in range(m):
            edges.append(list(map(int, input().rstrip().split())))

        s = int(input().strip())

        result = bfs(n, m, edges, s)

        fptr.write(" ".join(map(str, result)))
        fptr.write("\n")

    fptr.close()
