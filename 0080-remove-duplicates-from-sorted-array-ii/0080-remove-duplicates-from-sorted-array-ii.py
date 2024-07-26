class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        idx = 1
        num = nums[0]
        count = 1

        for i in range(1, len(nums)):
            if nums[i] == num and count < 2:
                nums[idx] = nums[i]
                idx += 1
                count += 1
            elif nums[i] != num:
                nums[idx] = nums[i]
                num = nums[i]
                count = 1
                idx +=1

        return idx


