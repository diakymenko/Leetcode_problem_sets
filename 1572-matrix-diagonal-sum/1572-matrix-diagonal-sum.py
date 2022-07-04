class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        sum_ = 0

        for i in range(len(mat)):
            sum_ += mat[i][i]
        print(sum_)

        for i in range(len(mat)):
            sum_ += mat[i][len(mat)-1 - i]
            print(mat[i][len(mat)-1 - i])

        if len(mat) % 2 != 0:
            mid = mat[len(mat)//2][len(mat)//2]
            sum_ -= mid

        return sum_
                