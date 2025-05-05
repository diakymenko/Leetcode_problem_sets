class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        def helper(i, j, board):
            if i > len(board) - 1 or j > len(board[i]) -1 or i < 0 or j < 0:
                return
            if board[i][j] == "X":
                board[i][j] = "."
                helper(i+1, j, board)
                helper(i-1, j, board)
                helper(i, j-1, board)
                helper(i, j+1, board)
        
        count = 0
        for i in range(len(board)):
            for j in range(len(board[i])):
                if board[i][j] == "X":
                    board[i][j] == "."
                    count += 1
                    helper(i+1, j, board)
                    helper(i-1, j, board)
                    helper(i, j-1, board)
                    helper(i, j+1, board)
        return count

