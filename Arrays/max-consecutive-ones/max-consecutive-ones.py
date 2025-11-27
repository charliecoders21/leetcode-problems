from typing import List
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        res = 0
        count = 0

        for n in nums:
            if n == 0:
                count = 0
            else:
                count += 1
            
            if res < count:
                res = count
        
        return res
    
print(Solution.findMaxConsecutiveOnes(self="",nums = [1,1,0,1,1,1]))