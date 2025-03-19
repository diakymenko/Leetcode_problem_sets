class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        set_nums = set(range(1, len(nums) +1))
        print(set_nums)
        
        res = []

        for num in nums:
            if num in set_nums:
                set_nums.remove(num)
        return list(set_nums)

