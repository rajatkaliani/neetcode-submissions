class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # initialize all lists of sets
        row = []
        col = []
        box = []
        for i in range(len(board)):
            row.append(set())
            col.append(set())
            box.append(set())
        for r in range(len(board)):
            for c in range(len(board[0])):
                b = (r // 3)*3 + (c//3)
                num = board[r][c]
                if num == ".":
                    continue
                else:
                    if num in row[r] or num in col[c] or num in box[b]:
                        return False
                    row[r].add(num)
                    col[c].add(num)
                    box[b].add(num)
        return True

            