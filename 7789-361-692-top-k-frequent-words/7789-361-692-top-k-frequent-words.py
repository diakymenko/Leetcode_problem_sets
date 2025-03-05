class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        dict_ = {}
        for word in words:
            dict_.setdefault(word, 0)
            dict_[word] += 1
        
        lst = sorted(dict_.items(), key=lambda x: (-x[1], x[0]))
        
        res = []
        for i in range(k):
            res.append(lst[i][0])
        return res

