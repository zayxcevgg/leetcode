# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        mid = len = head
        while len and len.next:
            mid = mid.next
            len = len.next.next
        return mid
 