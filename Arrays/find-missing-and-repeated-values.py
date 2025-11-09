from typing import List


class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        n = len(grid)
        count = {}
        repeated = missing = -1
        
        # Count occurrences
        for row in grid:
            for num in row:
                count[num] = count.get(num, 0) + 1
        
        # Find repeated and missing
        for num in range(1, n * n + 1):
            if num not in count:
                missing = num
            elif count[num] == 2:
                repeated = num
        
        return [repeated, missing]

    
print(Solution.findMissingAndRepeatedValues(self="",grid = [[9,1,7],[8,9,2],[3,4,6]]))
        