# You are given two positive integers num and sum.

# A positive integer n is good if it satisfies both of the following:

# The number of digits in n is exactly num.
# The sum of digits in n is exactly sum.
# The score of a good integer n is the sum of the squares of digits in n.

# Return a string denoting the good integer n that achieves the maximum score. If there are multiple possible integers, return the maximum ​​​​​​​one. If no such integer exists, return an empty string.

def maxSumOfSquares(num: int, sum: int) -> str:
    if sum<=0 or sum>9*num:
        return ""
    q,r=divmod(sum,9)
    if r==0:
        return "9"*q + "0"*(num-q)
    return "9"*q + str(r) + "0"*(num-q-1)
    
if __name__ == "__main__":
    # to maximise sos, include as bigger nums as possible in string representation
    num = 2
    sum = 3
    print(maxSumOfSquares(num, sum))