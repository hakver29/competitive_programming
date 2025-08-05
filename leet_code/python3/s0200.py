import unittest
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        islands = 0
        self.grid = grid
        rows, cols = len(grid), len(grid[0])

        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c):
            if (
                r < 0
                or r >= rows
                or c < 0
                or c >= cols
                or self.grid[r][c] == "0"
                or self.grid[r][c] == "#"
            ):
                return

            self.grid[r][c] = "#"

            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                dfs(new_r, new_c)

        for r in range(rows):
            for c in range(cols):
                if self.grid[r][c] == "1":
                    islands += 1
                    dfs(r, c)

        return islands


class TestSolution(unittest.TestCase):
    def test_numIslands1(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["1", "1", "1", "1", "0"],
                    ["1", "1", "0", "1", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "0", "0", "0"],
                ]
            ),
            1,
        )

    def test_numIslands2(self):
        self.assertEqual(
            Solution().numIslands(
                [
                    ["1", "1", "0", "0", "0"],
                    ["1", "1", "0", "0", "0"],
                    ["0", "0", "1", "0", "0"],
                    ["0", "0", "0", "1", "1"],
                ]
            ),
            3,
        )


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
