#!/bin/python3

#
# Complete the 'roadsAndLibraries' function below.
#
# The function is expected to return a LONG_INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. INTEGER c_lib
#  3. INTEGER c_road
#  4. 2D_INTEGER_ARRAY cities
#
import heapq
import os


def roadsAndLibraries(n, c_lib, c_road, cities):
    # Case 1: Library is cheaper or equal to a road.
    if c_lib <= c_road:
        return n * c_lib

    # Build the adjacency list with 0-based indexing
    adj = [[] for _ in range(n)]
    for u, v in cities:
        adj[u - 1].append(v - 1)
        adj[v - 1].append(u - 1)

    visited = [False] * n
    total_cost = 0

    # Iterate through all cities to find disconnected components
    for i in range(n):
        if not visited[i]:
            # This is a new component, so we must build one library
            total_cost += c_lib

            # Run Prim's algorithm on this component
            mst_cost = 0
            num_edges = 0

            # Use a min-priority queue (heap)
            pq = [(0, i)]  # (cost, node)

            while pq:
                cost, u = heapq.heappop(pq)

                if visited[u]:
                    continue

                visited[u] = True
                mst_cost += cost
                num_edges += 1

                if num_edges == n:
                    break

                for v in adj[u]:
                    if not visited[v]:
                        heapq.heappush(pq, (c_road, v))

            # Add the cost of the MST to the total cost
            total_cost += mst_cost

    return total_cost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        c_lib = int(first_multiple_input[2])

        c_road = int(first_multiple_input[3])

        cities = []

        for _ in range(m):
            cities.append(list(map(int, input().rstrip().split())))

        result = roadsAndLibraries(n, c_lib, c_road, cities)

        fptr.write(str(result) + "\n")

    fptr.close()
