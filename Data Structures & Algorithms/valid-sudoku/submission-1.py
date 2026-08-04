class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rowDict = []
        colDict = []
        TRow = []
        [colDict.append([])for i in range(0, len(board[0]))]
        [TRow.append([]) for i in range(0, 9)]
        for i in range(0, len(board)):
            curRow = []
            thirdRow = (i // 3) * 3
            for j in range(0, len(board[i])):
                if board[i][j] != '.':
                    if board[i][j] in curRow:
                        return False
                    elif board[i][j] in colDict[j]:
                        return False
                    elif board[i][j] in TRow[thirdRow + (j // 3)]:
                        return False
                    curRow.append(board[i][j])
                    colDict[j].append(board[i][j])
                    TRow[thirdRow + (j // 3)].append(board[i][j])
        return True

        