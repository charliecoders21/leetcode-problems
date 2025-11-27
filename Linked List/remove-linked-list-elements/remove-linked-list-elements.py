from ListNode import ListNode
from typing import Optional
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        curr=ListNode(0,head)
        dummy=curr
        while dummy:
            while dummy.next and dummy.next.val==val:
                dummy.next=dummy.next.next
            dummy=dummy.next
        return curr.next


def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


values = [1,2,6,3,4,5,6]
head = build_linked_list(values)

print(Solution.removeElements(self="",head=head,val=6))