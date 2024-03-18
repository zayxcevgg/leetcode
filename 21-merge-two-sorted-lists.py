# Definition for singly-linked list.
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = pointer = ListNode()
        while list1 and list2:
            if list1.val > list2.val:
                pointer.next = list2
                list2 = list2.next
            else:
                pointer.next = list1
                list1 = list1.next
            pointer = pointer.next
            pointer.next = list1 or list2
            print(dummy.next)
            return dummy.next

    
    list1 = [1,2,4]
    list2 = [1,3,4]
    mergeTwoLists(0, list1, list2)