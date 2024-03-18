from typing import Optional

#Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        length = 0
        while head != 0:
            head = head.next
            len +=1
        
        if length % 2 == 0:
            pointer = length / 2 + 1
        else:
            pointer = length / 2 + 0.5
        
        return head[(int(pointer)-1):]

    middleNode(0, [1,2,3,4,5,6])