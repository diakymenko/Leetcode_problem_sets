class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        elif x == 0:
            return True
        
        new_str = ""
        n = x
        res = None

        while n > 0:
            number = n % 10
            n = n // 10
            new_str += str(number)
        
        res = int(new_str)

        return res == x
        