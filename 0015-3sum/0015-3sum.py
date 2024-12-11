class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        set_res = set()
        nums.sort()

        res = []
        for i in range(len(nums)):
            j = i + 1
            k = len(nums) - 1
            if i > 0 and nums[i-1] == nums[i]:
                continue
            while j < k:
                total = nums[i] + nums[j] + nums[k]
                if total > 0:
                    k -= 1
                elif total < 0:
                    j += 1
                else:
                    set_res.add(tuple((sorted([nums[i], nums[j], nums[k]]))))
                    j+= 1
            
        for i in set_res:
            res.append(list(i))

        return res

       