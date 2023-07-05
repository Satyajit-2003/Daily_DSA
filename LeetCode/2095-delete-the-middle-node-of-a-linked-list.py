# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        fast = head
        slow = head
        prev_slow = None
        while (fast and fast.next):
            prev_slow = slow
            slow = slow.next
            fast = fast.next.next
        if slow and prev_slow:
            prev_slow.next = slow.next
            return head
        return None

if __name__ == "__main__":
    s=Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.deleteMiddle(head)
    while head:
        print(head.val, end=' ')
        head = head.next