class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        rem = 1
        
        for i in range(len(digits) -1, -1, -1):
            num = digits[i] + rem
            if num > 9:
                digits[i] = 0
                rem = 1
            else:
                digits[i] = num
                rem = 0
        return digits if rem == 0 else [1] + digits
        
            

        
            
        
        