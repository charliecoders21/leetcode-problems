from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        low=0
        high=len(s)-1
        while low<high:
            temp=s[high]
            s[high]=s[low]
            s[low]=temp
            low+=1
            high-=1
        
        
