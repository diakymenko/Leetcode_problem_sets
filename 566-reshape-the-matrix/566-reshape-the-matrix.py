class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        if r * c == len(mat[0]) * len(mat):
            new_lst = []
            index = 0
            idx_counter = 0
            for i in range(r):
                new_lst.append([])

            for i in range (len(mat)):
                for j in range (len(mat[i])):
                    if idx_counter < c and len(new_lst[index]) < c:
                        new_lst[index].append(mat[i][j])
                        idx_counter += 1
                    elif idx_counter >= c:
                        index += 1
                        new_lst[index].append(mat[i][j])
                        idx_counter = 0
                    else:
                        index += 1
                        new_lst[index].append(mat[i][j])
                        idx_counter = 0
            mat = copy.deepcopy(new_lst)
            return mat

        else:
            return mat