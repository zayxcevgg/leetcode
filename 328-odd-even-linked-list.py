# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def oddEvenList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head

        odd_head = head
        even_head = head.next
        odd = odd_head
        even = even_head

        while even is not None and even.next is not None:            
            odd.next = even.next
            odd = odd.next
            print(odd.val)

            even.next = odd.next
            even = even.next
            print(even.val)

        odd.next = even_head
        return odd_head


    head = ListNode(1, ListNode(2,  ListNode(3,  ListNode(4,  ListNode(5)))))
    oddEvenList(0, head)