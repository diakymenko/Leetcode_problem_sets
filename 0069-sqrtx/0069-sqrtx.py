class Solution:
    def mySqrt(self, x: int) -> int:
        
        if x == 1:
            return 1
        prev = None
        for i in range(x // 2 + 1):
            if i * i <= x:
                prev = i
            else:
                return prev
        return prev