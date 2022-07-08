class Solution:
    def romanToInt(self, s: str) -> int:
        dict_ = {"I": 1,
        "V": 5,
        "X": 10,
        "L": 50,
        "C": 100,
        "D": 500,
        "M": 1000}
        
        number = 0
        if len(s) == 1:
            return dict_[s[0]]
        
        for i in range(1, len(s)):
            if dict_[s[i]] <= dict_[s[i-1]]:
                number += dict_[s[i-1]]
            else:
                number-=dict_[s[i-1]]
            if i == len(s) - 1:
                number += dict_[s[i]]
        return number
            