import unittest


class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.strip(" ")
        sign = 0

        if len(s) == 0 or (len(s) == 1 and s not in "0123456789"):
            return 0

        if s[0] == "-":
            sign = -1
            s = s[1:]
        elif s[0] == "+":
            sign = 1
            s = s[1:]
        elif s[0] not in "0123456789":
            return 0
        else:
            sign = 1

        while s[0] == "0":
            s = s[1:]

        if len(s) == 0 or (len(s) == 1 and s not in "0123456789"):
            return 0

        for i in range(len(s)):
            if i == 0 and s[i] not in "0123456789":
                return 0
            if s[i] not in "0123456789":
                a = sign * int(s[:i])
                if a > 2**31 - 1:
                    return 2**31 - 1
                elif a < -(2**31):
                    return -(2**31)
                return a

        a = sign * int(s)
        if a > 2**31 - 1:
            return 2**31 - 1
        elif a < -(2**31):
            return -(2**31)
        return a


class TestCases(unittest.TestCase):
    def test_case1(self):
        self.assertEqual(Solution().myAtoi("42"), 42)

    def test_case2(self):
        self.assertEqual(Solution().myAtoi(" -042"), -42)

    def test_case3(self):
        self.assertEqual(Solution().myAtoi("1337c0d3"), 1337)

    def test_case4(self):
        self.assertEqual(Solution().myAtoi("+-12"), 0)

    def test_case5(self):
        self.assertEqual(Solution().myAtoi("21474836460"), 2147483647)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
