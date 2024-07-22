class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # res = []
        # set_unique = set()

        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         for k in range(j+1, len(nums)):
        #             if nums[i] + nums[j] + nums[k] == 0:
        #                 lst = [nums[i],nums[j],nums[k]]
        #                 lst.sort()
        #                 key = str(lst[0]) + "," + str(lst[1]) + "," + str(lst[2])
        #                 if key not in set_unique:
        #                     set_unique.add(key)
        #                     res.append(lst)
        
        # return res

        answer = set()
        nums.sort()
        target = 0
        for i in range(len(nums)):
            lo = i + 1
            hi = len(nums) -1
            a = nums[i]
            while lo < hi:
                if a + nums[lo] + nums[hi] < target:
                    # too small, increase sum
                    lo += 1
                elif a + nums[lo] + nums[hi] > target:
                    # too large, decrase sum
                    hi -= 1
                else:
                    # equals target
                    answer.add(tuple([a, nums[lo], nums[hi]]))
                    lo += 1
                    hi -= 1
        return answer