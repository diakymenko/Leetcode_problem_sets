class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        prev = arr[0]
        count = 0
        
        if len(arr) < 3:
            return False
        
        for i in range(1, len(arr)):
            if arr[i] > prev and count == 0:
                count += 1
            elif arr[i] == prev:
                return False
            elif arr[i] < prev and count == 1:
                count+= 1
            elif arr[i] < prev and count == 0:
                return False
            elif arr[i] > prev and count > 1:
                return False
            prev = arr[i]
        
        return True if count == 2 else False