# Given the root of a binary tree, return its maximum depth.

# A binary tree's maximum depth is the number of nodes along the longest path from the root node down to the farthest leaf node.

 

# Example 1:


# Input: root = [3,9,20,null,null,15,7]
# Output: 3

class Solution:
    def maxDepth(self, root: TreeNode | None) -> int:
        if not root:
            return 0
        depth=0
        level=[root]
        while level:
            depth+=1
            level=[child for node in level for child in (node.left, node.right) if child]
        return depth