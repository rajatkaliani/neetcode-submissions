class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        perm = ""
        visited = set()
        def bfs(index,i,j):
            if i < 0 or j < 0 or i >= len(board) or j >= len(board[0]) or board[i][j] != word[index] or (i,j) in visited:
                return False
            if index == len(word) - 1:
                perm = "bob"
                return True
            visited.add((i,j))
            a = bfs(index + 1,i+1,j)
            b = bfs(index + 1,i-1,j)
            c = bfs(index + 1,i,j+1)
            d = bfs(index + 1,i,j-1)
            visited.remove((i,j))
            if a or b or c or d:
                return True
        
        for i in range(len(board)):
            for j in range(len(board[0])):
                if bfs(0,i,j):
                    return True
        return False