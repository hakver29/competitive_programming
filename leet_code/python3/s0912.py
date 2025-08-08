import unittest
from collections import defaultdict
from typing import List


class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        numDict = defaultdict(int)
        for i in nums:
            numDict[i] += 1

        L = []
        sorted_keys = sorted(numDict.keys())
        for i in sorted_keys:
            count = numDict[i]
            for _ in range(count):
                L.append(i)
        return L


class TestClass(unittest.TestCase):
    def test_exampl1(self):
        self.assertEqual(Solution().sortArray([5, 2, 3, 1]), [1, 2, 3, 5])

    def test_exampl2(self):
        self.assertEqual(Solution().sortArray([5, 1, 1, 2, 0, 0]), [0, 0, 1, 1, 2, 5])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
