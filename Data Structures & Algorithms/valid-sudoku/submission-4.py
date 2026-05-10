class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #rows
        for row in board:
            dupes = set()
            for elm in row:
                if elm in dupes and elm != ".":
                    return False
                dupes.add(elm)
        #columns
        dupes = {}
        for i in range(len(board)):
            for j in range(len(board)):
                if j in dupes:
                    dupes[j].append(board[i][j])
                else:
                    dupes[j] = [board[i][j]]
        for sets in dupes.values():
            duplicates = set()
            for num in sets:
                if num in duplicates:
                    return False
                if num != ".":
                    duplicates.add(num)
        #squares
        for i in range(int(len(board)/3)):
            for j in range(int(len(board)/3)):
                dupes = set()
                for row in range(3):
                    for col in range(3):
                        if board[i*3 +row][j*3+col] in dupes:
                            return False
                        if board[i*3 +row][j*3 +col] != ".":
                            dupes.add(board[i*3 + row][j*3 +col])
    
      
        return True

            