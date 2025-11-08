class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=max_length=0
        my_set=set()
        for item in range(len(s)):
            while s[item] in my_set:
                my_set.remove(s[left])
                left+=1
            my_set.add(s[item])
            max_length=max(max_length,item-left+1)
        return max_length