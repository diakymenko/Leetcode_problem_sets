class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = []

        sorted_lst = sorted(strs, key=len)

        for i in range(len(sorted_lst[0])):
            char = sorted_lst[0][i]
            res.append(char)
            for j in range(len(sorted_lst)):
                if sorted_lst[j][i] != char:
                    return "".join(res[:-1])
        return "".join(res)
        

