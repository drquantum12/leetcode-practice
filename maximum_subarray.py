# Given an integer array nums, find the subarray with the largest sum, and return its sum.

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

# concept : enlarge sub array until next term increases current sum else restart

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sum=0
        cur_sum=0
        for i,j in enumerate(nums):
            cur_sum