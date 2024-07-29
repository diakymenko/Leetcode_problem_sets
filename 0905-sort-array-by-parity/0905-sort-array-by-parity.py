class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:
        r = len(nums) - 1
        l = 0

        while l < r:
            if nums[l] % 2 != 0 and nums[r] % 2 == 0:
                nums[r], nums[l] = nums[l], nums[r]
                r -= 1
                l += 1
            elif nums[l] % 2 == 0:
                l += 1
            elif nums[r] % 2 != 0:
                r -= 1
        return nums

            
