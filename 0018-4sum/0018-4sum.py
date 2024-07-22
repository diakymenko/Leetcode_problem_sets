class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        answer = set()
        nums.sort()

        for a in range(len(nums)):
            for b in range(a+1, len(nums)):
                hi = len(nums) - 1
                low = b + 1
                while low < hi:
                    if nums[a] + nums[b] + nums[low] + nums[hi] < target:
                        low += 1
                    elif nums[a] + nums[b] + nums[low] + nums[hi] > target:
                        hi-= 1
                    else:
                        answer.add(tuple([nums[a], nums[b], nums[low], nums[hi]]))
                        low += 1
                        hi -= 1
        return answer

                    

        