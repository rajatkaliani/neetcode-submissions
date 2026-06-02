class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        def dfs(i,j):
            if i < 0 or j < 0 or i > len(grid)-1 or j > len(grid[0])-1 or grid[i][j] == 0:
                return 0
            grid[i][j] = 0
            right = dfs(i+1,j)
            left = dfs(i-1,j)
            up = dfs(i,j+1)
            down = dfs(i,j-1)
            return 1 + right + left + up + down
        maxi = 0
        temp = 0 
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                temp = dfs(i,j)
                maxi = max(maxi,temp)
        return maxi
