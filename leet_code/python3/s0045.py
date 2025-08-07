import unittest
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = [0 for i in nums]
        for i in range(len(nums)):
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                elif jumps[i + j] == 0:
                    jumps[i + j] = max(jumps[i] + 1, jumps[+j])
                else:
                    jumps[i + j] = min(jumps[i] + 1, jumps[i + j])
        return jumps[-1]


class TestMySqrt(unittest.TestCase):
    def test_exampl1(self):
        self.assertEqual(Solution().jump([2, 3, 1, 1, 4]), 2)

    def test_example2(self):
        self.assertEqual(Solution().jump([2, 3, 0, 1, 4]), 2)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
