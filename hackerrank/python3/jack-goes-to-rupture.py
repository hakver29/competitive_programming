#!/bin/python3


#
# Complete the 'getCost' function below.
#
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

import heapq


def getCost(g_nodes, g_from, g_to, g_weight):
    dist = [float("inf") for i in range(g_nodes + 1)]
    start_node = 1
    dist[start_node] = 0
    adj_list = {i: [] for i in range(1, g_nodes + 1)}
    pq = [(0, start_node)]

    # Iterate through the edge lists and populate the adjacency list.
    for i in range(len(g_from)):
        u = g_from[i]
        v = g_to[i]
        w = g_weight[i]
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for w_v, v in adj_list[u]:
            d = max(current_dist, w_v)
            if d < dist[v]:
                dist[v] = d
                heapq.heappush(pq, (d, v))
    return dist[g_nodes]


if __name__ == "__main__":
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
#!/bin/python3


#
# Complete the 'getCost' function below.
#
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


def getCost(g_nodes, g_from, g_to, g_weight):
    dist = [float("inf") for i in range(g_nodes + 1)]
    start_node = 1
    dist[start_node] = 0
    adj_list = {i: [] for i in range(1, g_nodes + 1)}
    pq = [(0, start_node)]

    for i in range(len(g_from)):
        u = g_from[i]
        v = g_to[i]
        w = g_weight[i]
        adj_list[u].append((w, v))
        adj_list[v].append((w, u))

    while pq:
        current_dist, u = heapq.heappop(pq)
        if current_dist > dist[u]:
            continue
        for w_v, v in adj_list[u]:
            d = max(current_dist, w_v)
            if d < dist[v]:
                dist[v] = d
                heapq.heappush(pq, (d, v))
    if dist[g_nodes] == float("inf"):
        return "NO PATH EXISTS"
    return dist[g_nodes]


if __name__ == "__main__":
    g_nodes, g_edges = map(int, input().rstrip().split())

    g_from = [0] * g_edges
    g_to = [0] * g_edges
    g_weight = [0] * g_edges

    for i in range(g_edges):
        g_from[i], g_to[i], g_weight[i] = map(int, input().rstrip().split())

    getCost(g_nodes, g_from, g_to, g_weight)
