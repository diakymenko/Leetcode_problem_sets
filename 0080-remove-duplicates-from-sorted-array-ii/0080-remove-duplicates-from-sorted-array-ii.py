class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        val = nums[0]
        idx = 1
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == val and count < 2:
                count += 1
                nums[idx] = nums[i]
                idx += 1
            elif nums[i] != val:
                val = nums[i]
                nums[idx] = nums[i]
                count = 1
                idx += 1
        return idx



        