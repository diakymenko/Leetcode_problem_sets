class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        def is_valid(board, n, k, f, d, case):
            set_num = set()
            for i in range(n, k):
                for j in range(f, d):
                    if case == 'row' or case == "square":
                        if board[i][j] != ".":
                            if int(board[i][j]) < 10 and int(board[i][j]) not in set_num:
                                set_num.add(int(board[i][j]))
                            else:
                                return False
                    elif case == "column":
                        if board[j][i] != ".":
                            if int(board[j][i]) < 10 and int(board[j][i]) not in set_num:
                                set_num.add(int(board[j][i]))
                            else:
                                return False
                if case == 'row' or case == 'column':
                    set_num.clear()
            set_num.clear()
            return True
        
        #check rows
        #check columns
        # check squares 3x3
    
        
        
        
        if is_valid(board, 0, 9,0, 9, "row") and is_valid(board, 0, 9, 0, 9, "column") and is_valid(board, 0, 3, 0, 3, "square") and is_valid(board, 0, 3, 3, 6, "square") and is_valid(board, 0, 3, 6, 9, "square") and is_valid(board, 3, 6, 0, 3, "square") and is_valid(board, 3, 6, 3, 6, "square") and is_valid(board, 3, 6, 6, 9, "square") and is_valid(board, 6, 9, 0, 3, "square") and is_valid(board, 6, 9, 3, 6, "square") and is_valid(board, 6, 9, 6, 9, "square"):
            return True
        
        
        return False
        
      
            
    
    
    

                    
    
        