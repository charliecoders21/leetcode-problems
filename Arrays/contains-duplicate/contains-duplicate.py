from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        my_set=set()
        for n in nums:
            if my_set in n:
                return True
            my_set.add(n)
        return False