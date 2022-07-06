class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        number = -200
        for i in range(len(nums)):
            if nums[i] != number:
                nums[k] = nums[i]
                number = nums[i]
                k += 1
        return k