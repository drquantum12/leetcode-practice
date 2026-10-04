# Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

# The following rules define a valid string:

# Any left parenthesis '(' must have a corresponding right parenthesis ')'.
# Any right parenthesis ')' must have a corresponding left parenthesis '('.
# Left parenthesis '(' must go before the corresponding right parenthesis ')'.
# '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 

# Example 1:

# Input: s = "()"
# Output: true
# Example 2:

# Input: s = "(*)"
# Output: true
# Example 3:

# Input: s = "(*))"
# Output: true

class Solution:
    def checkValidString(self, s: str) -> bool:
        min_open=0
        max_open=0
        for i in s:
            if i=="(":
                min_open+=1
                max_open+=1
            elif i==")":
                min_open-=1
                max_open-=1
            else:
                min_open-=1    # as )
                max_open+=1     # as (

            if max_open<0:
                return False
            if min_open<0:
                min_open=0
        return min_open==0