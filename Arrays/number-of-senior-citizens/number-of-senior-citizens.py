from typing import List
class Solution:
    def countSeniors(self, details: List[str]) -> int:
        count=0
        for i in details:
            s=i[11:13]
            sint=int(s)
            if sint>60:
                count+=1
        return count
    
print(Solution.countSeniors(self="",details = ["7868190130M7522","5303914400F9211","9273338290F4010"]))