class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        dict_nums = {}
        for number in nums:
            if number in dict_nums:
                dict_nums[number] += 1
            else:
                dict_nums.setdefault(number, 1)
        counter = 0

        for number in nums:
            if (k - number) in dict_nums:
                counter += 1
                if dict_nums[k - number] == 1:
                    del dict_nums[k - number]
                elif dict_nums[k - number] > 1:
                    dict_nums[k - number] -= 1
                    
        return counter // 2

            