class Solution:
    def isValid(self, s: str) -> bool:
        par = {
            "]": "[",
            "}": "{",
            ")": "(",
        }
        lst = []
        for item in s:
            if item not in par:
                lst.append(item)
            else:
                if len(lst) == 0:
                    return False
                last = lst.pop()
                if par.get(item) != last:
                    return False

        return len(lst) == 0