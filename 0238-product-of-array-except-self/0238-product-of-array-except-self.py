class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        left_product = [1]*len(nums)
        right_product = [1]*len(nums)
        res = []

        for i in range(1, len(nums)):
            left_product[i] = left_product[i-1] * nums[i-1]
        print(left_product)
        
        for i in range(len(nums)-2, -1, -1):
            right_product[i] = right_product[i+1] * nums[i+1]
        print(right_product)
        
        for i in range(len(nums)):
            res.append(right_product[i] * left_product[i])
        
        return res