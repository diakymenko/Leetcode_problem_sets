class Solution:
    def isPalindrome(self, x: int) -> bool:
        
        if x < 0:
            return False
        elif x == 0:
            return True
        
        new_lst = []
        n = x

        while n > 0:
            number = n % 10
            n = n // 10
            new_lst.append(str(number))
        
        res = int("".join(new_lst))

        return res == x
        