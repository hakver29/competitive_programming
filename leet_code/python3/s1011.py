import unittest
from typing import List


class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        solutionFound = False
        lowerBound = int(sum(weights) / days)
        shipMaxWeight = lowerBound

        while solutionFound is False:
            currentDay = 1
            currentShipWeight = 0
            for i in weights:
                if i > shipMaxWeight:
                    currentDay = days + 1
                    break
                elif i + currentShipWeight > shipMaxWeight:
                    currentDay += 1
                    currentShipWeight = i
                else:
                    currentShipWeight += i

            if currentDay <= days:
                solutionFound = True
            else:
                shipMaxWeight += 1

        return shipMaxWeight


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
