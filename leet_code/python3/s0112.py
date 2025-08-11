import unittest
from typing import Optional

from utils.common import TreeNode


class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        if root is None:
            return False
        elif root.val == targetSum and root.left is None and root.right is None:
            return True
        else:
            hasPathSumLeft = self.hasPathSum(root.left, targetSum - root.val)
            hasPathSumRight = self.hasPathSum(root.right, targetSum - root.val)
            return hasPathSumLeft or hasPathSumRight


class TestSolution(unittest.TestCase):
    def test_tree1(self):
        targetSum = 5

        root = TreeNode(1)
        root.left = TreeNode(2)
        root.right = TreeNode(3)

        self.assertEqual(Solution().hasPathSum(root, targetSum), False)

    def test_tree2(self):
        targetSum = 0
        root = TreeNode()

        self.assertEqual(Solution().hasPathSum(root, targetSum), False)

    def test_tree3(self):
        targetSum = 22

        root = TreeNode(5)
        root.left = TreeNode(4)
        root.left.left = TreeNode(11)
        root.left.left.left = TreeNode(7)
        root.left.left.right = TreeNode(2)
        root.right = TreeNode(8)
        root.right.left = TreeNode(13)
        root.right.right = TreeNode(4)
        root.right.right.right = TreeNode(1)

        self.assertEqual(Solution().hasPathSum(root, targetSum), True)


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
