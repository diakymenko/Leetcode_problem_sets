class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        lst = []
        if len(s) == 1:
            return False
        
        for char in s:
            if char in par:
                if len(lst) > 0:
                    if lst[len(lst)-1] != par[char]:
                        return False
                    elif lst[len(lst)-1] == par[char]:
                        lst.pop()
                else:
                    return False
            else:
                lst.append(char)
        return len(lst) == 0
                
        