class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def dfs(row,col):
            if row < 0 or col < 0 or col > len(grid[0]) - 1 or row > len(grid) - 1 or grid[row][col] == "0":
                return
            else:
                grid[row][col] = "0"
                dfs(row+1,col)
                dfs(row-1,col)
                dfs(row,col+1)
                dfs(row,col-1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == "1":
                    count = count + 1
                    dfs(r,c)
        return count