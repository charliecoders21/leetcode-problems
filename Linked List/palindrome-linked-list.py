from typing import Optional
from ListNode import ListNode
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        # Step 1
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # Step 2        
        node = None
        while slow:
            temp = slow.next
            slow.next = node
            node = slow
            slow = temp
        
        # Step 3        
        first, second = head, node

        while second:
            if first.val != second.val:
                return False
            
            first = first.next
            second = second.next
        
        return True
        

head1=ListNode.list_to_linkedlist([1,2,2,1])
print(Solution.isPalindrome(self="",head=head1))