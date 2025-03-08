class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        col_dict = {}
        row_dict = {}
        box_dict = {}

        N = len(board[0])

        for row in range(N):
            for col in range(N):
                elem = board[row][col]
                if elem != ".":
                    if elem in col_dict.get(col, set()) or elem in row_dict.get(row, set()) or elem in box_dict.get((row // 3, col // 3), set()):
                        return False
                    row_dict.setdefault(row, set()).add(elem)
                    col_dict.setdefault(col, set()).add(elem)
                    box_dict.setdefault((row // 3, col // 3), set()).add(elem)
        return True
                    
            
            
            

                            
            
                