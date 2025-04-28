class Solution:
    def romanToInt(self, s: str) -> int:
        book = {
    'I': 1,
    'V': 5,
    'X': 10,
    'L': 50,
    'C': 100,
    'D': 500,
    'M': 1000
    }

        prev = book[s[0]]
        res = prev

        for i in range(1, len(s)):
            curr = book[s[i]]
            if curr > prev:
               res -= prev
               res += (curr-prev)
            else:
                res += curr
            prev = curr
        return res


    
    