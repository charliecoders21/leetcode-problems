class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        end = len(s) - 1

        while s[end] == " ":
            end -= 1
        
        start = end
        while start >= 0 and s[start] != " ":
            start -= 1
        
        return end - start
    
class Second:
    def lengthOfLastWord(self, s: str) -> int:
        s1=s.split(" ")
        for i in range(len(s1)-1,-1,-1):
            if s1[i]=="":
                continue
            else:
                return len(s1[i])
                
        return 0
    
print(Second.lengthOfLastWord(self="",s = "   fly me   to   the moon  "))