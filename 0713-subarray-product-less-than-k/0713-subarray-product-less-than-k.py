class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        
        if k <= 1:
            return 0
            
        curr = 1
        res = 0
        L = 0

        for R in range(len(nums)):
            curr *= nums[R]
            while curr >= k:
                curr //= nums[L]
                L+= 1
            res += R-L + 1
        return res
