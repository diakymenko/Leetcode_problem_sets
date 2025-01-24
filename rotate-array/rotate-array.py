class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        def helper(lst, start, finish):
            print(start, finish)
            while start < finish:
                lst[start], lst[finish] = lst[finish], lst[start]
                start += 1
                finish -=1
        """
        Do not return anything, modify nums in-place instead.
        """
        
        k = k % len(nums)
        rotate_idx = len(nums) - k
        helper(nums, 0, rotate_idx - 1)
        helper(nums, rotate_idx, len(nums) - 1)
        helper(nums, 0, len(nums) -1)

        
        