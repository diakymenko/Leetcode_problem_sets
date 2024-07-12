class Solution:
    def countGoodSubstrings(self, s: str) -> int:
        count = 0
        L = 0
        dict_ = {}

        for R in range(len(s)):
            dict_.setdefault(s[R], 0)
            dict_[s[R]] += 1
            if R-L + 1 == 3: #this is a condition for our window
                if len(dict_) == 3:
                    count += 1
                dict_[s[L]] -= 1
                if dict_[s[L]] == 0:
                    del dict_[s[L]]
                L+= 1     
        
        return count

