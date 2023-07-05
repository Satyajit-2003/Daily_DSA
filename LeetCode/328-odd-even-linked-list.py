from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not(head and head.next and head.next.next):
            return head
        
        eh_store = head.next
        oh = head
        eh = head.next

        while eh and eh.next:
            oh.next = oh.next.next
            oh = oh.next

            eh.next = eh.next.next
            eh = oh.next
        
        oh.next = eh_store
        return head 
    

if __name__ == "__main__":
    s = Solution()
    head = ListNode(1, ListNode(2, ListNode(3, ListNode(4, ListNode(5)))))
    head = s.oddEvenList(head)
    while head:
        print(head.val, end=' ')
        head = head.next
           
        