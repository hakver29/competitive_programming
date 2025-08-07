import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        n = len(nums)
        jumps = 0
        current_end = 0
        farthest = 0

        for i in range(n - 1):
            farthest = max(farthest, i + nums[i])

            if i == current_end:
                jumps += 1
                current_end = farthest

                if current_end >= n - 1:
                    break
        return jumps


class TestMySqrt(unittest.TestCase):
    def test_exampl1(self):
        self.assertEqual(Solution().jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(Solution().jump([2, 3, 0, 1, 4]), 2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
