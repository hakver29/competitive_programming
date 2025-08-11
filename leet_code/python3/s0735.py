import unittest
from typing import List


class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for i in asteroids:
            isDestroyed = False

            while len(stack) != 0 and stack[-1] > 0 and i < 0:
                if stack[-1] < abs(i):
                    stack.pop()
                elif stack[-1] == abs(i):
                    stack.pop()
                    isDestroyed = True
                    break
                else:
                    isDestroyed = True
                    break

            if isDestroyed is False:
                stack.append(i)

        return stack


class TestMySqrt(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().asteroidCollision([5, 10, -5]), [5, 10])

    def test_example2(self):
        self.assertEqual(Solution().asteroidCollision([8, -8]), [])

    def test_example3(self):
        self.assertEqual(Solution().asteroidCollision([10, 2, -5]), [10])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
