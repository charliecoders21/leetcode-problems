from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        low=max_area=0
        high=len(heights)-1
        
        while low<=high:
            width=high-low
            ht=min(heights[low],heights[high])
            curr_area=ht*width
            max_area=max(max_area,curr_area)
            if heights[low]<heights[high]:
                low+=1
            else:
                high-=1
        return max_area
    
print(Solution.maxArea(self="",heights = [1,7,2,5,4,7,3,6]))