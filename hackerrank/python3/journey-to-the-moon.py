#!/bin/python3

import os

#
# Complete the 'journeyToMoon' function below.
#
# The function is expected to return an INTEGER.
# The function accepts following parameters:
#  1. INTEGER n
#  2. 2D_INTEGER_ARRAY astronaut
#
from collections import defaultdict


def group_elements(n, data):
    # 1. Build the adjacency list
    adj_list = defaultdict(list)
    for a, b in data:
        adj_list[a].append(b)
        adj_list[b].append(a)

    groups = []
    visited = set()

    for i in range(n):
        if i not in visited:
            current_group_size = 0
            stack = [i]
            visited.add(i)

            while stack:
                node = stack.pop()
                current_group_size += 1

                # Explore neighbors
                for neighbor in adj_list[node]:
                    if neighbor not in visited:
                        visited.add(neighbor)
                        stack.append(neighbor)

            # 3. Store the found group
            groups.append(current_group_size)

    return groups


def journeyToMoon(n, astronaut):
    groups_size = group_elements(n, astronaut)
    total_pairs = n * (n - 1) // 2
    pairs_within_groups = 0
    for size in groups_size:
        pairs_within_groups += size * (size - 1) // 2
    return total_pairs - pairs_within_groups


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    p = int(first_multiple_input[1])

    astronaut = []

    for _ in range(p):
        astronaut.append(list(map(int, input().rstrip().split())))

    result = journeyToMoon(n, astronaut)

    fptr.write(str(result) + "\n")

    fptr.close()
