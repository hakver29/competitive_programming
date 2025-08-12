import unittest
from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = 0
        current = 0
        high = len(nums) - 1

        while current <= high:
            if nums[current] == 0:
                nums[current], nums[low] = nums[low], nums[current]
                low += 1
                current += 1
            elif nums[current] == 2:
                nums[current], nums[high] = nums[high], nums[current]
                high -= 1
            else:
                current += 1


class TestMySqrt(unittest.TestCase):
    def test_example_1(self):
        ex_1_input = [2, 0, 2, 1, 1, 0]
        ex_1_output = [0, 0, 1, 1, 2, 2]

        Solution().sortColors(ex_1_input)
        self.assertEqual(ex_1_input, ex_1_output)

    def test_example_2(self):
        ex_2_input = [2, 0, 1]
        ex_2_output = [0, 1, 2]

        Solution().sortColors(ex_2_input)
        self.assertEqual(ex_2_input, ex_2_output)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
