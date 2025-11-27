class Solution:
    def isPalindrome(self, s: str) -> bool:
        res=[]
        for item in s:
            if item.lower().isalnum():
                res.append(item.lower())
        return Solution.checkPalindrome(0,len(res)-1,res)
        
    def checkPalindrome(low,high,res)->bool:
        while low<high:
            if res[low]!=res[high]:
                return False
            low+=1
            high-=1
        return True
        