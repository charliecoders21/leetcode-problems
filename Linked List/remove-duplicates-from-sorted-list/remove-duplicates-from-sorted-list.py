from ListNode import ListNode
from typing import Optional
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res=head
        while head and head.next:
            if head.val==head.next.val:
                head.next=head.next.next
            else:
                head=head.next
        return res
    
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


values = [1,1,2]
head = build_linked_list(values)

print(Solution.deleteDuplicates(self="",head=head))