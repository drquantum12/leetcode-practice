def maxAlternatingSum(nums):
    n=len(nums)
    sm=sorted([i*i for i in nums], reverse=True)
    return sum(sm[:(n+1) // 2]) - sum(sm[(n+1) // 2:])
if __name__ == "__main__":
    nums=[1,2,3]
    maxAlternatingSum(nums)
