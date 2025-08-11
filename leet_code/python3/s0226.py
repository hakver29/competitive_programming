import unittest
from collections import deque
from typing import Optional

from utils.common import TreeNode


class Solution:
    def buildBinaryTreeFromList(self, nodes: list[Optional[int]]) -> Optional[TreeNode]:
        if not nodes:
            return None
        if nodes[0] is None:
            return None

        root = TreeNode(nodes[0])
        queue = deque([root])
        i = 1

        while queue and i < len(nodes):
            current_node = queue.popleft()

            if i < len(nodes) and nodes[i] is not None:
                current_node.left = TreeNode(nodes[i])
                queue.append(current_node.left)
            i += 1

            if i < len(nodes) and nodes[i] is not None:
                current_node.right = TreeNode(nodes[i])
                queue.append(current_node.right)
            i += 1
        return root

    def buildListFromBinaryTree(self, root: Optional[TreeNode]) -> list[Optional[int]]:
        if not root:
            return []

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            result.append(node.val if node else None)

            if node:
                queue.append(node.left)
                queue.append(node.right)

        while result and result[-1] is None:
            result.pop()

        return result

    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return None

        left_inverted = self.invertTree(root.left)
        right_inverted = self.invertTree(root.right)

        root.left = right_inverted
        root.right = left_inverted

        return root

    def invertBinaryTreeFromInput(
        self, root: list[Optional[int]]
    ) -> list[Optional[int]]:
        binaryTree = self.buildBinaryTreeFromList(root)
        invertedBinaryTree = self.invertTree(binaryTree)
        invertedBinaryTreeList = self.buildListFromBinaryTree(invertedBinaryTree)
        return invertedBinaryTreeList


class TestMySqrt(unittest.TestCase):
    def test_complex_case(self):
        self.assertEqual(
            Solution().invertBinaryTreeFromInput([4, 2, 7, 1, 3, 6, 9]),
            [4, 7, 2, 9, 6, 3, 1],
        )

    def test_simple_case(self):
        self.assertEqual(Solution().invertBinaryTreeFromInput([2, 1, 3]), [2, 3, 1])

    def test_empty_tree(self):
        self.assertEqual(Solution().invertBinaryTreeFromInput([]), [])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-ignored"], exit=False)
