# Definition for singly-linked list.
from math import gcd
from typing import Optional

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
class Solution:
    def insertGreatestCommonDivisors(self, values: Optional[ListNode]) -> Optional[ListNode]:
        if not values:
            return None
        
        # Create the linked list from the input list
        head = ListNode(values[0])
        current = head
        for val in values[1:]:
            current.next = ListNode(val)
            current = current.next
        
        # Insert GCD nodes
        itr = head
        while itr and itr.next:
            p = itr.val
            q = itr.next.val
            gcd_val = gcd(p, q)
            new_node = ListNode(gcd_val, itr.next)
            itr.next = new_node
            itr = new_node.next
        
        # Print the linked list
        current = head
        elements = []
        while current:
            elements.append(current.val)
            current = current.next
        print(elements)
        
        #return head

    
    values = [18,6,10,3]
    insertGreatestCommonDivisors(0, values)
        