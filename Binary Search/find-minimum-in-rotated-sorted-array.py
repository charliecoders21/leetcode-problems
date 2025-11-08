from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        low=0
        high=len(nums)-1
        while low<high:
            mid=low+(high-low)//2
            if nums[mid]<=nums[high]:
                high=mid
            else:
                low=mid+1
        return nums[low]
    
print(Solution.findMin(self="",nums = [3,4,5,1,2]))