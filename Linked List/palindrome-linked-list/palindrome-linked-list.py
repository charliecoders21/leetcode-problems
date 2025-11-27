from ListNode import ListNode
from typing import Optional
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
    

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    curr = head
    for v in values[1:]:
        curr.next = ListNode(v)
        curr = curr.next
    return head


values = [1, 2, 2, 1]
head = build_linked_list(values)

print(Solution.isPalindrome(self="",head=head))


    
