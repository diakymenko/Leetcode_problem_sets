class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        if len(matrix) == 0:
            return False
        elif len(matrix[0]) == 1:
            return True
        
        for i in range(len(matrix)-1):
            for j in range(len(matrix[0])-1):
                num = matrix[i][j]
                print(num)
                if matrix[i+1][j+1] != num:
                    return False
        return True