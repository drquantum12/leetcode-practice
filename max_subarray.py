# Given an integer array nums, find the subarray with the largest sum, and return its sum.

 

# Example 1:

# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: The subarray [4,-1,2,1] has the largest sum 6.

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        c_sum=0
        m_sum=nums[0]
        for i in nums:
            c_sum+=i
            if c_sum>m_sum:
                m_sum=c_sum
            if c_sum<0:
                c_sum=0
        return m_sum