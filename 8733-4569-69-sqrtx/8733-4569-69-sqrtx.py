class Solution:
    def mySqrt(self, x: int) -> int:

        if x == 1 or x == 0:
            return x

        start = 1
        end = x
        temp = 0

        while start <= end:
            mid = (start + end) // 2
            if mid * mid < x:
                temp = mid
                start = mid + 1
            elif mid * mid > x:
                end = mid - 1
            else:
                return mid
        return temp
        