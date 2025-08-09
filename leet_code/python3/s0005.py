import unittest


class Solution:
    def longestPalindrome(self, s: str) -> str:
        k = 0
        case = ""
        for i in range(len(s)):
            for left, right in [(i, i), (i, i + 1)]:
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if (right - left + 1) > k:
                        case = s[left : right + 1]
                        k = right - left + 1
                    left -= 1
                    right += 1

        return case


class TestCases(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(Solution().longestPalindrome("babad"), "bab")

    def test_example2(self):
        self.assertEqual(Solution().longestPalindrome("cbbd"), "bb")

    def test_example3(self):
        self.assertEqual(Solution().longestPalindrome("a"), "a")


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
