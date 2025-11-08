from ListNode import ListNode
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        curr=dummy
        while list1 and list2:
            if list1>list2:
                curr.next=list2
                list2=list2.next
            else:
                curr.next=list1
                list1=list1.next
            curr=curr.next
        if list1:
            curr.next=list1
        else:
            curr.next=list2
        return dummy.next
    
head1=ListNode.list_to_linkedlist([1,2,4])
head2=ListNode.list_to_linkedlist([1,3,4])
print(Solution.mergeTwoLists(self="",list1 = head1,list2=head2))
            