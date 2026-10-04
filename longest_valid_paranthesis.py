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




# class Solution:
#     def longestValidParentheses(self, s: str) -> int:
#         max_cnt=0
#         left=0
#         right=0
#         for i in range(0,len(s)):
#             if s[i]=="(":
#                 left+=1
#             else:
#                 right+=1
#             if left==right:
#                 max_cnt=max(max_cnt, 2*right)
#             elif right>left:
#                 right=0
#                 left=0
#         left=0
#         right=0
#         for i in range(len(s)-1,-1,-1):
#             if s[i]=="(":
#                 left+=1
#             else:
#                 right+=1
#             if left==right:
#                 max_cnt=max(max_cnt, 2*left)
#             elif left>right:
#                 right=0
#                 left=0
            
#         return max_cnt