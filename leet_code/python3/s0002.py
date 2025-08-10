from typing import Optional


class ListNode:
    def __iinit__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        dummy_head = ListNode(0)
        tail = dummy_head
        carry = 0
        while l1 is not None and l2 is not None:
            current_node = ListNode((l1.val + l2.val + carry) % 10)
            carry = (l1.val + l2.val + carry) // 10
            tail.next = current_node
            tail = tail.next
            l1 = l1.next
            l2 = l2.next

        while l1 is not None:
            current_node = ListNode((l1.val + carry) % 10)
            carry = (l1.val + carry) // 10
            tail.next = current_node
            tail = tail.next
            l1 = l1.next

        while l2 is not None:
            current_node = ListNode((l2.val + carry) % 10)
            carry = (l2.val + carry) // 10
            tail.next = current_node
            tail = tail.next
            l2 = l2.next

        if carry > 0:
            tail.next = ListNode(carry)

        return dummy_head.next
