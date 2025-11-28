from collections import defaultdict
from typing import List
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans=defaultdict(list)
        for item in strs:
            key="".join(sorted(item))
            ans[key].append(item)
        return list(ans.values())
            