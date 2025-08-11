import unittest
from typing import Optional

from utils.common import TreeNode


class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        if p is None and q is None:
            return True
        elif p is None and q is not None:
            return False
        elif p is not None and q is None:
            return False
        else:
            isNodesSame = p.val == q.val
            isLeftSameTree = self.isSameTree(p.left, q.left)
            isRightSameTree = self.isSameTree(p.right, q.right)
            return isNodesSame and isLeftSameTree and isRightSameTree


class TestSolution(unittest.TestCase):
    def test_tree1(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(3)

        q = TreeNode(1)
        q.left = TreeNode(2)
        q.right = TreeNode(3)
        self.assertEqual(Solution().isSameTree(p, q), True)

    def test_tree2(self):
        p = TreeNode(1)
        p.left = TreeNode(2)

        q = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(Solution().isSameTree(p, q), False)

    def test_tree3(self):
        p = TreeNode(1)
        p.left = TreeNode(2)
        p.right = TreeNode(1)

        q = TreeNode(1)
        q.left = TreeNode(1)
        q.right = TreeNode(2)
        self.assertEqual(Solution().isSameTree(p, q), False)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
