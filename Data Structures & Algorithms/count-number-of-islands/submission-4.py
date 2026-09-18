class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(r,c):
            if r < 0 or c < 0 or c > len(grid[0])-1 or r > len(grid)-1:
                return
            if grid[r][c] == "0":
                return
            elif grid[r][c] == "1":
                grid[r][c]= "0"
                dfs(r+1,c)
                dfs(r-1,c)
                dfs(r,c+1)
                dfs(r,c-1)
        count = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == "1":
                    count+=1
                    dfs(row,col)
        return count