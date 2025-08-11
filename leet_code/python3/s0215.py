import unittest
from typing import List


class Solution:
    def heapify(self, arr, n, i):
        largest = i
        left_child = 2 * i + 1
        right_child = 2 * i + 2

        if left_child < n and arr[largest] < arr[left_child]:
            largest = left_child

        if right_child < n and arr[largest] < arr[right_child]:
            largest = right_child

        if largest != i:
            arr[i], arr[largest] = arr[largest], arr[i]

            self.heapify(arr, n, largest)

    def findKthLargest(self, nums: List[int], k: int) -> int:
        n = len(nums)
        for i in range(n // 2 - 1, -1, -1):
            self.heapify(nums, n, i)

        for i in range(n - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            self.heapify(nums, i, 0)
        return nums[-k]


class TestCases(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().findKthLargest([3, 2, 1, 5, 6, 2], 2), 5)

    def test_example2(self):
        self.assertEqual(Solution().findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
