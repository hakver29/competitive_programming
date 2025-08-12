import heapq
import unittest
from typing import List


class Solution:
    def get_neighbours(self, n, edges, succProb):
        neighbours = []
        for e in range(len(edges)):
            [u, v] = edges[e]
            if u == n:
                neighbours.append([v, succProb[e]])
            elif v == n:
                neighbours.append([u, succProb[e]])
        return neighbours

    def maxProbability(
        self,
        n: int,
        edges: List[List[int]],
        succProb: List[float],
        start_node: int,
        end_node: int,
    ) -> float:
        prob = []
        priority_queue = []

        for i in range(n):
            prob.append(-1)

        prob[start_node] = 1
        heapq.heappush(priority_queue, (1, start_node))

        while len(priority_queue) > 0:
            n = heapq.heappop(priority_queue)
            if n[0] < prob[n[1]]:
                continue

            neighbours = self.get_neighbours(n[1], edges, succProb)
            for u, pr in neighbours:
                p = prob[n[1]] * pr

                if p > prob[u]:
                    prob[u] = p
                    heapq.heappush(priority_queue, (p, u))
        if prob[end_node] == -1:
            return 0.0
        return prob[end_node]


class TestCases(unittest.TestCase):
    def test_case_1(self):
        self.assertEqual(
            Solution().maxProbability(
                3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.2], 0, 2
            ),
            0.25000,
        )

    def test_case_2(self):
        self.assertEqual(
            Solution().maxProbability(
                3, [[0, 1], [1, 2], [0, 2]], [0.5, 0.5, 0.3], 0, 2
            ),
            0.30000,
        )

    def test_case_3(self):
        self.assertEqual(Solution().maxProbability(3, [[0, 1]], [0.5], 0, 2), 0.00000)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
