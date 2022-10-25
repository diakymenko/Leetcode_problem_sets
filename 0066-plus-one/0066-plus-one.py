class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num = 1
        for i in range(len(digits)-1, -1, -1):
            num += digits[i] * 10 ** (len(digits) - 1 - i)
        
        lst = []
        
        num = str(num)
        return list(num)
            
            
            
            
            
        