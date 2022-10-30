class Solution:
    
    def helper(self, idx1, idx2, s):
        if idx1 >= idx2:
            return
        s[idx1], s[idx2] = s[idx2], s[idx1]
        self.helper(idx1+1, idx2-1, s)
    
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        pointer1 = 0
        pointer2 = len(s) - 1
        self.helper(pointer1, pointer2, s)
      