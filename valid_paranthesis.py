class Solution:
    def isValid(self, s: str) -> bool:
        stack=[]
        pairs={")":"(", "]":"[", "}":"{"}
        for i in s:
            if i in pairs:
                if not stack or stack.pop()!=pairs[i]:
                    return False
            else:
                stack.append(i)
        return not stack