from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        prev = None
        slow = fast = head

        while fast:
            fast = fast.next.next
            temp = slow
            slow = slow.next
            temp.next = prev
            prev = temp

        twin = 0
        while slow:
            twin = max(twin, slow.val+prev.val)
            slow = slow.next
            prev = prev.next

        return twin
    
if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(7, ListNode(5, ListNode(4))))))
    print(s.pairSum(head))
