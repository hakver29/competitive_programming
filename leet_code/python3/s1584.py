import heapq
import unittest
from typing import List


class Solution:
    def manhattan_distance(self, point1, point2):
        return abs(point1[0] - point2[0]) + abs(point1[1] - point2[1])

    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        mst_edges = []
        mst_nodes = []
        priority_queue = []

        start = points[0]
        mst_nodes.append(start)

        for i in range(1, len(points)):
            heapq.heappush(
                priority_queue, (self.manhattan_distance(start, points[i]), points[i])
            )

        while len(mst_nodes) < len(points):
            u = heapq.heappop(priority_queue)
            if u[1] not in mst_nodes:
                mst_nodes.append(u[1])
                mst_edges.append(u[0])

                for j in points:
                    if j not in mst_nodes:
                        heapq.heappush(
                            priority_queue, (self.manhattan_distance(j, u[1]), j)
                        )

        return sum(mst_edges)


class TestCases(unittest.TestCase):
    def test_example_1(self):
        self.assertEqual(
            Solution().minCostConnectPoints([[0, 0], [2, 2], [3, 10], [5, 2], [7, 0]]),
            20,
        )

    def test_example_2(self):
        self.assertEqual(
            Solution().minCostConnectPoints([[3, 12], [-2, 5], [-4, 1]]), 18
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
