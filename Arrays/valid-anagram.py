class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False
        s_dict={}
        t_dict={}
        for i in range(len(s)):
            s_dict[s[i]]=1+s_dict.get(s[i])
            t_dict[t[i]]=1+t_dict.get(t[i])
        return s_dict==t_dict
        