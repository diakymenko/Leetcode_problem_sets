class Solution:
    def frequencySort(self, s: str) -> str:
        dict_ = {}

        for char in s:
            dict_[char] = dict_.get(char, 0) + 1
        
        dict_counter = {}

        for char, count in dict_.items():
            dict_counter[count] = dict_counter.get(count, []) + [char]

        res = []
        for count in range(len(s), 0, -1):
            for char in dict_counter.get(count, []):
                res.append(char*count)
        return "".join(res)



