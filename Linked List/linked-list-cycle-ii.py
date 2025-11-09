from ListNode import ListNode
from typing import Optional
class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        seen=set()
        while head:
            if head in seen:
                return head
            seen.add(head)
            head=head.next
        return None
    
head1=ListNode.list_to_linkedlist([3,2,0,-4])
print(Solution.detectCycle(self="",head=head1))