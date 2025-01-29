class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_ = {}
        
        for i in range(len(nums)):
            dict_[nums[i]] = i
        
        for i in range(len(nums)):
            if target - nums[i] in dict_ and dict_[target - nums[i]] != i:
                return [i, dict_[target - nums[i]]]
                