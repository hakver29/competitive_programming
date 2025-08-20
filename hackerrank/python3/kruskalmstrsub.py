#!/bin/python3

import os

#
# Complete the 'kruskals' function below.
#
# The function is expected to return an INTEGER.
# The function accepts WEIGHTED_INTEGER_GRAPH g as parameter.
#

#
# For the weighted graph, <name>:
#
# 1. The number of nodes is <name>_nodes.
# 2. The number of edges is <name>_edges.
# 3. An edge exists between <name>_from[i] and <name>_to[i]. The weight of the edge is <name>_weight[i].
#
#


class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, i):
        if self.parent[i] == i:
            return i
        self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            # Union by size
            if self.size[root_i] < self.size[root_j]:
                root_i, root_j = root_j, root_i
            self.parent[root_j] = root_i
            self.size[root_i] += self.size[root_j]
            return True
        return False


def kruskals(g_nodes, g_from, g_to, g_weight):
    edges = []
    for i in range(len(g_from)):
        u, v, w = g_from[i], g_to[i], g_weight[i]
        edges.append((w, min(u, v), max(u, v)))
    edges.sort()
    dsu = DSU(g_nodes)
    mst_cost = 0

    for w, u, v in edges:
        if dsu.union(u - 1, v - 1):
            mst_cost += w
    return mst_cost


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    res = kruskals(g_nodes, g_from, g_to, g_weight)

    fptr.write(str(res) + "\n")
    fptr.close()
