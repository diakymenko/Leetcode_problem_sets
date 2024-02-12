class Solution:
    def duplicateZeros(self, arr: List[int]) -> None:
        """
        Do not return anything, modify arr in-place instead.
        """
        count = 0
        idx = 0
        idx_to_place = len(arr)-1
        
        for i in range(len(arr)):
            if arr[i] == 0:
                count += 1
            count+=1
            if count == len(arr):
                idx = i
                break
            elif count > len(arr):
                arr[idx_to_place] = 0
                idx_to_place -= 1
                idx = i-1
                break
        
                
        for i in range(idx, -1, -1):
          
            if arr[i] == 0:
                arr[idx_to_place] = 0
                idx_to_place -= 1
                arr[idx_to_place] = 0
                idx_to_place -= 1
            else:
                arr[idx_to_place] = arr[i]
                idx_to_place -= 1
                
                