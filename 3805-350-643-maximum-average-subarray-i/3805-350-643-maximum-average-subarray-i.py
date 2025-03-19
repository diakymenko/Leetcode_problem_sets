class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        if k == len(nums):
            return sum(nums) /k
        
        sum_num = sum(nums[:k])
        max_sum = sum_num
        start = 0
       
        for i in range(1, len(nums)-k +1):
            j = i + k-1
            if j < len(nums):
                sum_num = sum_num - nums[start] + nums[j]
                start = i
                max_sum = max(sum_num, max_sum)
        return max_sum / k
