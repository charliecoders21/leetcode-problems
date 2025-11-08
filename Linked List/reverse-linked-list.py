from ListNode import ListNode
from typing import Optional
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev=None
        curr=head
        while curr:
            next=curr.next
            curr.next=prev
            prev=curr
            curr=next
        return prev


head1=ListNode.list_to_linkedlist([1,2,3,4,5])
print(Solution.reverseList(self="",head = head1))