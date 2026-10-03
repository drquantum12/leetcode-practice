# Given a VPS seq, split it into two disjoint subsequences A and B, such that A and B are VPS's (and A.length + B.length = seq.length). The subsequences may not necessarily be contiguous.

# For example, for the sequence 123456789, one possible split is:

# A = {1, 3, 5, 7, 9},

# B = {2, 4, 6, 8}.

# This corresponds to the output [0, 1, 0, 1, 0, 1, 0, 1, 0]  where 0 indicates membership in A and 1 indicates membership in B.

# Now choose any such A and B such that max(depth(A), depth(B)) is the minimum possible value.

# Return an answer array (of length seq.length) that encodes such a choice of A and B:  answer[i] = 0 if seq[i] is part of A, else answer[i] = 1.  Note that even though multiple answers may exist, you may return any of them.

 

# Example 1:

# Input: seq = "(()())"
# Output: [0,1,1,1,1,0]
# Example 2:

# Input: seq = "()(())()"
# Output: [0,0,0,1,1,0,1,1]
 

# Constraints:

# 1 <= seq.size <= 10000


class Solution:
    def maxDepthAfterSplit(self, seq: str) -> list[int]:
        res = []
        d=0
        for i in seq:
            if i=="(":
                d^=1
                res.append(d)
            else:
                res.append(d)
                d^=1

        return res