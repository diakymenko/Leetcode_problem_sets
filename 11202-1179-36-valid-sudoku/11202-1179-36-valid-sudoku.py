class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:

        def grids_valid(board):
            for i in range(len(board)):
                for j in range(len(board[i])):
                    if int(i) % 3 == 0 and int(j) % 3 == 0:
                        set_ = set()
                        for k in range(i, i + 3):
                            for m in range(j, j + 3):
                                if board[k][m] in set_:
                                    print(set_)
                                    return False
                                else:
                                    if board[k][m] != ".":
                                        set_.add(board[k][m])
            return True

        def rows_valid(board):
            for i in range(len(board)):
                set_ = set()
                for j in range(len(board[i])):
                    if board[i][j] in set_:
                        return False
                    else:
                        if board[i][j] != ".":
                            set_.add(board[i][j])
            return True

        def columns_valid(board):
            for j in range(len(board[0])):
                set_ = set()
                for i in range(len(board)):
                    if board[i][j] in set_:
                        return False
                    else:
                        if board[i][j] != ".":
                            set_.add(board[i][j])
            return True

        return grids_valid(board) and rows_valid(board) and columns_valid(board)
