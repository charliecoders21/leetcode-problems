from typing import List
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        my_dict={}
        for k,v in enumerate(nums):
            if target-v in my_dict:
                return [k,my_dict.get(target-v)]
            my_dict[v]=k
    
print(Solution.twoSum(self="",nums = [2,7,11,15], target = 9))
    
    