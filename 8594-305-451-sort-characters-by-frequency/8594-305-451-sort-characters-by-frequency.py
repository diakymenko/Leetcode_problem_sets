class Solution:
    def frequencySort(self, s: str) -> str:
        letters = {}
        for char in s:
            letters.setdefault(char, 0)
            letters[char] += 1
        
        #convert dict in a list of tuples
        lst = list(letters.items())
        #sort by frequency
        lst.sort(key=lambda x: x[1], reverse=True)
        
        res = []

        for tup in lst:
            for i in range(tup[1]):
                res.append(tup[0])
        return "".join(res)

