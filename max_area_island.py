# sol 1
class Solution:
    def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
        m=len(grid)
        n=len(grid[0])
        max_cnt=0
        def bfs(i,j):
            if i<0 or i>=m or j<0 or j>=n or grid[i][j]==0:
                return 0
            grid[i][j]=0
            return 1 + bfs(i-1,j) + bfs(i+1,j) + bfs(i,j-1) + bfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j]==1:
                    max_cnt=max(max_cnt, bfs(i,j))
        return max_cnt

# sol 2
# class Solution:
#     def maxAreaOfIsland(self, grid: list[list[int]]) -> int:
#         m=len(grid)
#         n=len(grid[0])
#         tmp_cnt=0
#         max_cnt=0
#         def bfs(i,j):
#             nonlocal tmp_cnt
#             tmp_cnt+=1
#             grid[i][j]=0
#             if i-1>=0 and grid[i-1][j]==1:
#                 bfs(i-1,j)
#             if j-1>=0 and grid[i][j-1]==1:
#                 bfs(i,j-1)
#             if i+1<m and grid[i+1][j]==1:
#                 bfs(i+1,j)
#             if j+1<n and grid[i][j+1]==1:
#                 bfs(i,j+1)
#             return
#         for i in range(m):
#             for j in range(n):
#                 if grid[i][j]==1:
#                     tmp_cnt=0
#                     bfs(i,j)
#                     if tmp_cnt>max_cnt:
#                         max_cnt=tmp_cnt
#         return max_cnt
