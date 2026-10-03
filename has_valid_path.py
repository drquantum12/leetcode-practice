global m,n, grid
mem = {}

def dfs(i,j,b):
    if (i > m-1) or (j > n-1):
        return False

    if grid[i][j] == "(":
        b+=1
    else:
        b-=1

    if b < 0 or b > (m+n-1)-(i+j+1):
        return False

    if i==m-1 and j ==n-1 and b==0:
        return True

    if (i,j+1, b) in mem:
        return mem[(i, j+1, b)]
    else:
        res=dfs(i, j+1, b)
        mem[(i, j+1, b)]=res
        if res:
            return True


    if (i+1,j, b) in mem:
        return mem[(i+1, j, b)]
    else:
        res=dfs(i+1, j, b)
        mem[(i+1, j, b)]=res
        if res:
            return True

    return False

if __name__ == "__main__":
    grid = [["(","(","("],[")","(",")"],["(","(",")"],["(","(",")"]]
    m,n = len(grid), len(grid[0])
    b=0
    if grid[0][0] == ")":
        print(False)
    print(dfs(0,0,b))



# fastest solution
# class Solution:
#     def hasValidPath(self, grid: list[list[str]]) -> bool:
#         m, n = len(grid), len(grid[0])

#         if grid[0][0] == ')' or grid[-1][-1] == '(':
#             return False

#         length = m + n - 1

#         # A valid parentheses string must have even length
#         if length & 1:
#             return False

#         # Maximum possible balance is length
#         mask = (1 << (length + 1)) - 1

#         # dp[j] is a bitset:
#         # bit k == 1  <=> balance k is reachable at (current_row, j)
#         dp = [0] * n

#         # Starting '(' gives balance = 1
#         dp[0] = 2

#         for i in range(m):
#             for j in range(n):
#                 if i == 0 and j == 0:
#                     continue

#                 # Reachable balances from top OR left
#                 bits = dp[j]
#                 if j:
#                     bits |= dp[j - 1]

#                 if not bits:
#                     dp[j] = 0
#                     continue

#                 if grid[i][j] == '(':
#                     # Every balance becomes balance + 1
#                     bits <<= 1
#                 else:
#                     # Every balance becomes balance - 1
#                     bits >>= 1

#                 # Remove impossible balances
#                 dp[j] = bits & mask

#         # Bit 0 means balance == 0 is reachable
#         return dp[-1] & 1 != 0