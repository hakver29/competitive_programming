#!/bin/python3

import heapq
import os

#
# Complete the 'prims' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY edges
#  3. INTEGER start
#


def prims(n, edges, start):
    visited = [False] * n
    start_node = start - 1

    adj = [[] for _ in range(n)]
    for u, v, w in edges:
        adj[u - 1].append((w, v - 1))
        adj[v - 1].append((w, u - 1))

    pq = [(0, start_node)]
    mst_cost = 0

    while pq:
        weight, u = heapq.heappop(pq)
        if visited[u]:
            continue

        visited[u] = True
        mst_cost += weight

        for w, v in adj[u]:
            if not visited[v]:
                heapq.heappush(pq, (w, v))
    return mst_cost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    edges = []

    for _ in range(m):
        edges.append(list(map(int, input().rstrip().split())))

    start = int(input().strip())

    result = prims(n, edges, start)

    fptr.write(str(result) + "\n")

    fptr.close()
