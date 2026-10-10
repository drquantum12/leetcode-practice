# You are given two positive 0-indexed integer arrays nums1 and nums2, both of length n.

# The sum of squared difference of arrays nums1 and nums2 is defined as the sum of (nums1[i] - nums2[i])2 for each 0 <= i < n.

# You are also given two positive integers k1 and k2. You can modify any of the elements of nums1 by +1 or -1 at most k1 times. Similarly, you can modify any of the elements of nums2 by +1 or -1 at most k2 times.

# Return the minimum sum of squared difference after modifying array nums1 at most k1 times and modifying array nums2 at most k2 times.

# Note: You are allowed to modify the array elements to become negative integers.

# Input: nums1 = [1,4,10,12], nums2 = [5,8,6,9], k1 = 1, k2 = 1
# Output: 43
# Explanation: One way to obtain the minimum sum of square difference is: 
# - Increase nums1[0] once.
# - Increase nums2[2] once.
# The minimum of the sum of square difference will be: 
# (2 - 5)2 + (4 - 8)2 + (10 - 7)2 + (12 - 9)2 = 43.
# Note that, there are other ways to obtain the minimum of the sum of square difference, but there is no way to obtain a sum smaller than 43.


class Solution:
    def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
        k=k1+k2
        diffs=[abs(i-j) for i,j in zip(nums1, nums2)]
        if sum(diffs) <=k:
            return 0

        m=(max(diffs)+1)
        res=[0]*m
        for i in diffs:

            res[i]+=1
        for i in range(m-1,0,-1):
            c=res[i]
            if c==0:
                continue
            if k>c:
                k-=c
                res[i-1]+=c
                res[i]=0
            else:
                res[i]-=k
                res[i-1]+=k
                k=0
                break
        return sum([(i*i*res[i]) for i in range(1,m) if res[i]])

# binary search based solution : 
# class Solution:
#     def minSumSquareDiff(self, nums1: list[int], nums2: list[int], k1: int, k2: int) -> int:
#         k=k1+k2
#         diffs=[abs(i-j) for i,j in zip(nums1, nums2)]
#         target_cap=0
#         ans=0
#         if sum(diffs) <=k:
#             return 0
#         low,high=0,max(diffs)
#         while low<=high:
#             mid=(low+high)//2
#             needed=sum([max(i-mid,0) for i in diffs])
#             if k>=needed:
#                 high=mid-1
#                 target_cap=mid
#             else:
#                 low=mid+1
#         k_rem=k-sum([max(i-target_cap,0) for i in diffs])
#         new_diffs=[min(target_cap, i) for i in diffs]
#         for i in new_diffs:
#             if i==target_cap and k_rem>0:
#                 val=i-1
#                 k_rem-=1
#             else:
#                 val=i
#             ans+=(val*val)
#         return ans