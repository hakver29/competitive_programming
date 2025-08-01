import unittest

class Solution:
    def mySqrt(self, x: int) -> int:
        if x < 0:
            raise ValueError("Input must be a non-negative integer.")
        return int(x**0.5) # A simple way to compute integer square root for testing purposes
       

class TestMySqrt(unittest.TestCase):
    def test_perfect_square_small(self):
        self.assertEqual(Solution().mySqrt(4), 2)

    def test_perfect_square_large(self):
        self.assertEqual(Solution().mySqrt(8), 2)

# This block allows you to run the tests directly from the script
if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)
