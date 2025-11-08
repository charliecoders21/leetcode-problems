class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        mapping={'}':'{',']':'[',')':'('}
        for item in s:
            if item in mapping.values():
                stack.append(item)
            elif item in mapping.keys():
                if not stack or stack.pop()!=mapping[item]:
                    return False
        return not stack