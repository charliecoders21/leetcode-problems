from typing import List
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        res=majority=0
        for item in nums:
            if majority==0:
                res=item
            majority+=1 if item==res else -1
        return res