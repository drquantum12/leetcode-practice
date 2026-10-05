# Given a balanced parentheses string s, return the score of the string.

# The score of a balanced parentheses string is based on the following rule:

# "()" has score 1.
# AB has score A + B, where A and B are balanced parentheses strings.
# (A) has score 2 * A, where A is a balanced parentheses string.


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        prev=""
        cnt=0
        depth=0
        for i,j in enumerate(s):
            if j=="(":
                depth+=1
            else:
                depth-=1
                if s[i-1]=="(":
                    cnt += 1<<depth
        return cnt