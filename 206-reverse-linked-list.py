# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import Optional


class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        rev_list = None
        pointer = head

        while pointer:
            next_node = pointer.next
            pointer.next = rev_list
            rev_list = pointer
            pointer = next_node

        return rev_list

    head = ListNode(1, ListNode(2,  ListNode(3,  ListNode(4,  ListNode(5)))))
    reverseList(0, head)