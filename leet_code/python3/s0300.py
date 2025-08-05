import unittest


class Solution:
    def lengthOfLIS(self, nums: []) -> int:
        dp = [1 for i in range(len(nums))]

        for i in range(len(dp)):
            for j in range(i):
                if nums[i] > nums[j]:
                    dp[i] = max(dp[j] + 1, dp[i])

        return max(dp)


class TestMySqrt(unittest.TestCase):
    def test_first_dummy_example(self):
        self.assertEqual(Solution().lengthOfLIS([10, 9, 2, 5, 3, 7, 101, 18]), 4)

    def test_second_dummy_example(self):
        self.assertEqual(Solution().lengthOfLIS([0, 1, 0, 3, 2, 3]), 4)

    def test_constant_sequence(self):
        self.assertEqual(Solution().lengthOfLIS([7, 7, 7, 7, 7, 7]), 1)


# This block allows you to run the tests directly from the script
if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
