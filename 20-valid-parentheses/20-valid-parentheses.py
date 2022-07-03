class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        lst = []
        if len(s) % 2 != 0:
            return False
        
        for char in s:
            if char in par:
                if len(lst) > 0:
                    if lst[-1] != par[char]:
                        return False
                    else:
                        lst.pop()
                else:
                    return False
            else:
                lst.append(char)
        return len(lst) == 0
                
        