import unittest
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(
        self, list1: Optional[ListNode], list2: Optional[ListNode]
    ) -> Optional[ListNode]:
        if list1 is None and list2 is None:
            return None
        elif list2 is None:
            return list1
        elif list1 is None:
            return list2

        dummy_head = ListNode(0)
        tail = dummy_head

        ptr1 = list1[0]
        ptr2 = list2[0]

        while ptr1 is not None and ptr2 is not None:
            if ptr1.val <= ptr2.val:
                tail.next = ptr1
                ptr1 = ptr1.next
                tail = ptr1
            elif ptr1.val > ptr2.val:
                tail.next = ptr2
                ptr2 = ptr2.next
                tail = ptr2

        if ptr1 is not None:
            tail.next = ptr1
        elif ptr2 is not None:
            tail.next = ptr2

        return dummy_head.next


class TestCases(unittest.TestCase):
    def test_example1(self):
        self.assertEqual(
            Solution().mergeTwoLists([1, 2, 4], [1, 3, 4]), [1, 1, 2, 3, 4, 4]
        )

    def test_example2(self):
        self.assertEqual(Solution().mergeTwoLists([], []), [])

    def test_example3(self):
        self.assertEqual(Solution().mergeTwoLists([], [0]), [0])


if __name__ == "__main__":
    unittest.main(argv=["first-arg-is-inored"], exit=False)
