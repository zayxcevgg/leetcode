from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow = fast = head
        prev = None
        while fast is not None and fast.next is not None:
            prev = slow
            slow = slow.next
            fast = fast.next.next
        
        if slow is not None and slow.next is not None:
            slow.val = slow.next.val
            slow.next = slow.next.next
        elif prev is not None:
            prev.next = None
        else:
            head = None

        return head
        
    

    head = ListNode(2, ListNode(1))

    deleteMiddle(0, head)