class Solution:
    def isPalindrome(self, s: str) -> bool:
        s="".join(c.lower() for c in s if c.isalnum())
        high=len(s)-1
        low=0
        while low<high:
            if s[low]!=s[high]:
                return False
            low+=1
            high-=1
        return True
    
print(Solution.isPalindrome(self="",s = "Was it a car or a cat I saw?"))
            