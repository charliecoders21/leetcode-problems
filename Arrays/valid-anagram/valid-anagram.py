class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict={}
        t_dict={}
        for item in range(len(s)):
            s_dict[s[item]]=1+s_dict.get(s[item],0)
            t_dict[t[item]]=1+t_dict.get(t[item],0)
        return s_dict==t_dict