from ListNode import ListNode
from typing import Optional
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        dummy=ListNode()
        res=dummy
        while list1 and list2:
            if list1.val>list2.val:
                res.next=list2
                list2=list2.next
            else:
                res.next=list1
                list1=list1.next
            res=res.next
        if list1:
            res.next=list1
        else:
            res.next=list2
        return dummy.next