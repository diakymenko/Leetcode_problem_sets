class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
     
        left_pointer = len(nums1) - len(nums2) - 1
        right_pointer = len(nums2) - 1
        to_place = len(nums1) - 1

        while to_place >= 0:
            if left_pointer < 0:
                nums1[to_place] = nums2[right_pointer]
                right_pointer -= 1
                to_place -= 1
            elif right_pointer < 0:
                nums1[to_place] = nums1[left_pointer]
                left_pointer -= 1
                to_place -= 1
            elif nums1[left_pointer] >= nums2[right_pointer]:
                nums1[to_place] = nums1[left_pointer]
                left_pointer -= 1
                to_place -= 1  
            else:
                nums1[to_place] = nums2[right_pointer]
                right_pointer -= 1
                to_place -= 1
        
        
