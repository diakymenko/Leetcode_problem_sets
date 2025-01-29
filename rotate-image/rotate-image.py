class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        # reverse sublists order in matrix

        l = 0
        r = len(matrix) - 1
        while l < r:
            matrix[r], matrix[l] = matrix[l], matrix[r]
            l += 1
            r -= 1
        
        for i in range(len(matrix)):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
