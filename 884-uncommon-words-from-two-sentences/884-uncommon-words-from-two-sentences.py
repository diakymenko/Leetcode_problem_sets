class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        s = s1.split() + s2.split()
        lst = []
        dict_1 = {}
        for word in s:
            if word in dict_1:
                dict_1[word] += 1
            else:
                dict_1.setdefault(word, 1)
        
        for word in s:
            if word in dict_1:
                if dict_1[word] == 1:
                    lst.append(word)

        return lst