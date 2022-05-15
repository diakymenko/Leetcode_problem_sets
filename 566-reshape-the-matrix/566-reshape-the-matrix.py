class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c != len(mat[0]) * len(mat):
            return mat

        res = []
        sub = []

        for i in range(len(mat)):
            for j in range(len(mat[i])):

                sub.append(mat[i][j])

                if len(sub) == c:
                    res.append(sub)
                    sub = []

        return res