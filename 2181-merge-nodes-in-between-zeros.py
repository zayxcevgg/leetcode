# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeNodes(self, head: ListNode) -> ListNode:
        dummy = ListNode(0)
        pointer = dummy
        counter = pointer
        while counter:
            sum = 0
            while counter.val != 0:
                sum += counter.val
                counter += counter.next
            pointer.val = sum

            counter = counter.next
            pointer.next = counter
            pointer = pointer.next
        print(head.next)
        return 0
    
    def create_linked_list(arr):
        dummy = ListNode(0)
        current = dummy
        for num in arr:
            current.next = ListNode(num)
            current = current.next
        return dummy.next

    def print_linked_list(head):
        current = head
        while current:
            print(current.val, end=' -> ' if current.next else '\n')
            current = current.next

    head = create_linked_list([0, 3, 1, 0, 4, 5, 2, 0])
    print("Original linked list: " + str(type(head)))
    print_linked_list(head)
    head = [0,3,1,0,4,5,2,0]
    mergeNodes(0, head)