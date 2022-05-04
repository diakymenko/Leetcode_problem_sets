class Solution:
    def validPalindrome(self, s: str) -> bool:
        idx_r = len(s) - 1

        for idx_l in range(len(s) // 2):
            if s[idx_l] != s[idx_r]:
                s_l = s[:idx_l] + s[(idx_l + 1):]
                s_r = s[:idx_r] + s[(idx_r + 1):]
                print(s_l, s_r)
                if s_l == s_l[::-1] or s_r == s_r[::-1]:
                    return True
                else:
                    return False
            else:
                idx_r -= 1
        return True
                
                
            
            
            
                