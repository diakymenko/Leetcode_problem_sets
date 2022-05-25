class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        new = ""
        for letter in s:
            if not letter.isalpha() and not letter.isnumeric():
                continue
            else:
                new = new + letter
        for i in range(len(new)//2):
            if new[i] != new[len(new) - 1 - i]:
                return False
        return True