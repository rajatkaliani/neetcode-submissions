class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        def bfs(row,col):
            if (row < 0 or col < 0 or row > len(grid)-1 or col > len(grid[0])-1):
                return
            if (grid[row][col] == '0'):
                return 
            grid[row][col] = '0'
            bfs(row-1,col)
            bfs(row+1,col)
            bfs(row,col-1)
            bfs(row,col+1)
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                print(grid[r][c])
                if grid[r][c] == '1':
                    bfs(r,c)
                    count += 1
        return count
