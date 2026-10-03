class Solution:
    def rob(self, nums: list[int]) -> int:
        ln = len(nums)
        if ln<2:
            return nums[0]
        if ln<3:
            return max(nums)
        
        dp0=nums[0]
        dp1=max(nums[0],nums[1])
        i=2
        while i<ln:
            dp=max(nums[i]+dp0, dp1)
            dp0=dp1
            dp1=dp
            i+=1
        return dp1

# house robber 2 : if houses are in circle

class Solution:
    def rob(self, nums: list[int]) -> int:
        lnt=len(nums)
        max_dp=0
        if lnt<4:
            return max(nums)
        for i in range(2):
            dp0=nums[i]
            dp1=max(nums[i:i+2])
            for j in range(i+2,lnt-1+i):
                dp=max(dp0+nums[j], dp1)
                dp0=dp1
                dp1=dp
            if dp1>max_dp:
                max_dp=dp1
            
        return max_dp
