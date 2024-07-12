class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        res = 0
        curr = 0
        dict_ = {}
        L = 0

        for R in range(len(nums)):
            dict_.setdefault(nums[R], 0)
            dict_[nums[R]] += 1
            curr += nums[R]
            if R-L + 1 == k:
                if len(dict_) == k:
                    res = max(res, curr)
                dict_[nums[L]] -= 1
                if dict_[nums[L]] == 0:
                    del dict_[nums[L]]
                curr -= nums[L]
                L+= 1
        return res
