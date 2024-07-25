class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:

       
        idx_place = len(nums1) - 1
        idx_1 = m-1
        idx_2 = n-1


        while idx_2 >= 0:
            if idx_1 >= 0 and nums1[idx_1] > nums2[idx_2]:
                nums1[idx_place] = nums1[idx_1]
                idx_1 -= 1
            else:
                nums1[idx_place] = nums2[idx_2]
                idx_2 -= 1
            idx_place -= 1


        
            






        
        