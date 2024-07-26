class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:

        idx_place = 1
        num = nums[0]

        for i in range(1, len(nums)):
            if nums[i] != num:
                nums[idx_place] = nums[i]
                idx_place += 1
                num = nums[i]
        return idx_place