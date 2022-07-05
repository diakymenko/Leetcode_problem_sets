class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        lst = []
        first = None
        last = None
        count = 0
        if len(nums) == 1:
            lst.append(str(nums[0]))
        for i in range(len(nums) - 1):
            if nums[i + 1] - nums[i] == 1:
                if count == 0:
                    first = nums[i]
                    last = nums[i + 1]
                    count += 1
                else:
                    last = nums[i + 1]
                if i == len(nums) - 2:
                    lst.append(f'{first}->{last}')
            elif nums[i + 1] - nums[i] > 1:
                if count == 0:
                    lst.append(str(nums[i]))
                else:
                    lst.append(f'{first}->{last}')
                    first,last,count = None,None,0
                if i == len(nums) - 2:
                    lst.append(str(nums[i + 1]))
        return lst