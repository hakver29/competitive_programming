import unittest

class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        rows, cols = len(board), len(board[0])
        
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]

        def dfs(r, c, idx):
            if idx == len(word):
                return True

            if (r < 0 or r >= rows or
                c < 0 or c >= cols or
                board[r][c] != word[idx]):
                return False

            original_char = board[r][c]
            board[r][c] = '#'

            found = False
            for dr, dc in directions:
                new_r, new_c = r + dr, c + dc
                if dfs(new_r, new_c, idx + 1):
                    found = True
                    break

            board[r][c] = original_char

            return found

        for r in range(rows):
            for c in range(cols):
                if board[r][c] == word[0]:
                    if dfs(r, c, 0):
                        return True

        return False



class TestMySqrt(unittest.TestCase):
    def test_word1(self):
        self.assertEqual(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCCED"), True)

    def test_word2(self):
        self.assertEqual(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "SEE"), True)

    def test_word3(self):
        self.assertEqual(Solution().exist([["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], "ABCB"), False)

if __name__ == '__main__':
    unittest.main(argv=['first-arg-is-ignored'], exit=False)

