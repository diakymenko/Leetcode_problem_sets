class Solution:
    def romanToInt(self, s: str) -> int:
        book = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        sum_num = 0
        curr = 0
        for i in range(len(s) - 1, -1, -1):
            if book[s[i]] < curr:
                sum_num -= book[s[i]]
            else:
                sum_num += book[s[i]]
            curr = book[s[i]]
        return sum_num
