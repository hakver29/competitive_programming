import unittest
from typing import List


class Solution:
    def checkCapacity(self, weights: List[int], days: int, capacity: int):
        day = 1
        currentWeight = 0
        for i in weights:
            if i + currentWeight > capacity:
                day += 1
                currentWeight = i
            else:
                currentWeight += i

        if day <= days:
            return True
        return False

    def shipWithinDays(self, weights: List[int], days: int) -> int:
        lowerBound = max(weights)
        upperBound = sum(weights)

        while lowerBound < upperBound:
            mid = lowerBound + ((upperBound - lowerBound) // 2)
            canHaveCapacity = self.checkCapacity(weights, days, mid)
            if canHaveCapacity is True:
                upperBound = mid
            else:
                lowerBound = mid + 1

        return lowerBound


class TestMySqrt(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            Solution().shipWithinDays([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5), 15
        )

    def test_example2(self):
        self.assertEqual(Solution().shipWithinDays([3, 2, 2, 4, 1, 4], 3), 6)

    def test_example3(self):
        self.assertEqual(Solution().shipWithinDays([1, 2, 3, 1, 1], 4), 3)


# This block allows you to run the tests directly from the script
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
