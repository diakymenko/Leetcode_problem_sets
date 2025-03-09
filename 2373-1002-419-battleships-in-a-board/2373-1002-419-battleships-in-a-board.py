class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        count = 0
        def helper(row, col, board):
            if row >= len(board) or col >= len(board[0]) or row < 0 or col < 0:
                return
            if board[row][col] == "X":
                board[row][col] = "."
                helper(row+1, col, board)
                helper(row-1, col, board)
                helper(row, col+1, board)
                helper(row, col-1, board)
           
        
        for row in range(len(board)):
            for col in range(len(board[row])):
                if board[row][col] == "X":
                    count+=1
                    helper(row, col, board)    
        return count
