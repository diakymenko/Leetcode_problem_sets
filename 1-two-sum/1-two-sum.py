class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dict_nums = {}
        
        lst = []
        
        for index, num in enumerate(nums):
            if target - num in dict_nums and dict_nums[target - num] != index:
                lst.append(index)
                lst.append(dict_nums[target - num])
                return lst
            else:
                dict_nums[num] = index
                
        
        