class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        res = []
        lst1 = list(word1)
        lst2 = list(word2)

        idx1 = 0
        idx2 = 0

        while idx1 < len(lst1) and idx2 < len(lst2):
            res.append(lst1[idx1])
            res.append(lst2[idx2])
            idx1 += 1
            idx2 += 1
        
        if idx1 < len(lst1):
            while idx1 < len(lst1):
                res.append(lst1[idx1])
                idx1 += 1
        elif idx2 < len(lst2):
            while idx2 < len(lst2):
                res.append(lst2[idx2])
                idx2 += 1
        return "".join(res)

        
  




        