# Given a string containing just the characters '(' and ')', return the length of the longest valid (well-formed) parentheses substring.

 

# Example 1:

# Input: s = "(()"
# Output: 2
# Explanation: The longest valid parentheses substring is "()".
# Example 2:

# Input: s = ")()())"
# Output: 4
# Explanation: The longest valid parentheses substring is "()()".

class Solution:
    def longestValidParentheses(self, s: str) -> int:
        stk=[-1]
        max_cnt=0
        for i, j in enumerate(s):
            if j=="(":
                stk.append(i)
            else:
                stk.pop()
                if not stk:
                    stk.append(i)
                else:
                    diff=i-stk[-1]
                    if diff>max_cnt:
                        max_cnt=diff
        return max_cnt