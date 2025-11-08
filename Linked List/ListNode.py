# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
        
    def list_to_linkedlist(items):
        head = ListNode(items[0])
        current = head
        for val in items[1:]:
            current.next = ListNode(val)
            current = current.next
        return head