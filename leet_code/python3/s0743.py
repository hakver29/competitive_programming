import heapq
import unittest


class Solution(object):
    def createGraphComplex(self, times, n):
        graph_complex = {}
        for i in range(n):
            graph_complex[i + 1] = []
            for j in range(len(times)):
                if times[j][0] == i + 1:
                    graph_complex[i + 1].append((times[j][2], times[j][1]))
        return graph_complex

    def networkDelayTime(self, times, n, k):
        """
        :type times: List[List[int]]
        :type n: int
        :type k: int
        :rtype: int
        """
        graph_complex = Solution().createGraphComplex(times, n)

        distances = [float("inf") for i in range(n)]
        distances[k - 1] = 0
        priority_queue = []
        heapq.heappush(priority_queue, (0, k))
        while priority_queue:
            current_node = heapq.heappop(priority_queue)
            if current_node[1] in graph_complex:
                edges = graph_complex[current_node[1]]
                for d, u in edges:
                    alt = distances[current_node[1] - 1] + d
                    if alt < distances[u - 1]:
                        distances[u - 1] = alt
                        heapq.heappush(priority_queue, (alt, u))
            else:
                pass
        if max(distances) == float("inf"):
            return -1
        else:
            return max(distances)


class TestMySqrt(unittest.TestCase):
    def test_complex_graph(self):
        self.assertEqual(
            Solution().createGraphComplex([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4),
            {1: [], 2: [(1, 1), (1, 3)], 3: [(1, 4)], 4: []},
        )

    def test_simple_graph(self):
        self.assertEqual(
            Solution().createGraphComplex([[1, 2, 1]], 2), {1: [(1, 2)], 2: []}
        )

    def test_simple_network(self):
        self.assertEqual(Solution().networkDelayTime([[1, 2, 1]], 2, 1), 1)

    def test_complex_network(self):
        self.assertEqual(
            Solution().networkDelayTime([[2, 1, 1], [2, 3, 1], [3, 4, 1]], 4, 2), 2
        )

    def test_faulty_network(self):
        self.assertEqual(Solution().networkDelayTime([[1, 2, 1]], 2, 2), -1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
