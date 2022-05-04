class Solution:
    def maxOperations(self, numbers: List[int], target: int) -> int:
        dict_nums = {}
        for num in numbers:
            if type(num) == int or type(num) == float:
                if num in dict_nums:
                    dict_nums[num] += 1
                else:
                    dict_nums.setdefault(num, 1)
            else:
                continue

        counter = 0

        for num in numbers:
            if type(num) == int or type(num) == float:
                if (target - num) in dict_nums:
                    counter += 1
                    if dict_nums[target - num] == 1:
                        del dict_nums[target - num]
                    elif dict_nums[target - num] > 1:
                        dict_nums[target - num] -= 1
            else:
                continue

        return counter // 2