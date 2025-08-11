import unittest
from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach = 0
        for i in range(len(nums)):
            if i > max_reach:
                return False
            max_reach = max(max_reach, i + nums[i])
            if max_reach >= len(nums) - 1:
                return True
        return False


class TestMySqrt(unittest.TestCase):
    def test_exampl1(self):
        self.assertEqual(Solution().canJump([2, 3, 1, 1, 4]), True)

    def test_example2(self):
        self.assertEqual(Solution().canJump([3, 2, 1, 0, 4]), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
