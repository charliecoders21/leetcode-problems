from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        majority=res=0
        for i in nums:
            
            if majority==0:
                res=i
            majority+=1 if res==i else -1
        return res