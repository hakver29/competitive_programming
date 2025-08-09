import unittest
from typing import List


class Solution:
    def maxList(self, nums: List[int]) -> float:
        if len(nums) == 0:
            return -float("inf")
        return max(nums)

    def minList(self, nums: List[int]) -> float:
        if len(nums) == 0:
            return float("inf")
        return min(nums)

    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        isOdd = (n + m) % 2 == 1
        low = 0
        high = n

        if n > m:
            temp = nums2
            nums2 = nums1
            nums1 = temp
            n = len(nums1)
            m = len(nums2)
            high = n

        i = (low + high) // 2
        j = (m + n + 1) // 2 - i

        [p1x, p2x] = [nums1[:i], nums1[i:]]
        [p1y, p2y] = [nums2[:j], nums2[j:]]

        while (
            self.maxList(p1x) <= self.minList(p2y)
            and self.maxList(p1y) <= self.minList(p2x)
        ) is False:
            if self.maxList(p1y) > self.minList(p2x):
                low = i + 1
                i = (low + high) // 2
                j = (n + m + 1) // 2 - i
            else:
                high = i - 1
                i = (low + high) // 2
                j = (n + m + 1) // 2 - i

            [p1x, p2x] = [nums1[:i], nums1[i:]]
            [p1y, p2y] = [nums2[:j], nums2[j:]]

        if isOdd is True:
            return max(self.maxList(p1x), self.maxList(p1y))
        else:
            return (
                max(self.maxList(p1x), self.maxList(p1y))
                + min(self.minList(p2x), self.minList(p2y))
            ) / 2


class TestCases(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().findMedianSortedArrays([1, 2], [3, 4]), 2.5)

    def test_example2(self):
        self.assertEqual(Solution().findMedianSortedArrays([1, 3], [1, 2, 3]), 2)

    def test_example3(self):
        self.assertEqual(
            Solution().findMedianSortedArrays(
                [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]
            ),
            7.5,
        )

    def test_example4(self):
        self.assertEqual(Solution().findMedianSortedArrays([1, 3], [2]), 2)

    def test_example5(self):
        self.assertEqual(
            Solution().findMedianSortedArrays(
                [1, 2, 3, 4, 5], [6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17]
            ),
            9,
        )

    def test_example6(self):
        self.assertEqual(
            Solution().findMedianSortedArrays(
                [1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]
            ),
            7.5,
        )

    def test_example7(self):
        self.assertEqual(Solution().findMedianSortedArrays([], [1]), 1)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
