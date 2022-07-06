class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        k = 0
        number = None
        count = 0
        for i in range(len(nums)):
            if nums[i] == number and count < 2:
                nums[k] = nums[i]
                number = nums[i]
                k+=1
                count+=1
            elif nums[i] != number:
                count = 1
                nums[k] = nums[i]
                number = nums[i]
                k+=1
        return k