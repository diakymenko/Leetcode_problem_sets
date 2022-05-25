class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for letter in s:
            if not letter.isalpha() and not letter.isnumeric():
                continue
            else:
                new = new + letter
        if len(new) == 1:
            return True
        return new == new[::-1]