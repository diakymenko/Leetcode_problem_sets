class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        set1 = set()
        count = 0
        for number in arr:
            set1.add(number)
        
        for i in range(1, arr[len(arr)-1]):
            if i not in set1:
                count += 1
                if count == k:
                    return i
        
        diff = k - count
        return arr[len(arr) -1] + diff
            
            
        