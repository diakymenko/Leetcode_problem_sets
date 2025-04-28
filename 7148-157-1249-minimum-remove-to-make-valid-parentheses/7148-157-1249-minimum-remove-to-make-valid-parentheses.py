class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        res = []

        for i in range(len(s)):
            if s[i] == "(":
                res.append(s[i])
                stack.append(i)
            elif s[i] == ")":
                if len(stack) > 0:
                    stack.pop()
                    res.append(s[i])
                else:
                    #add to keep cnsistency with idx in stack
                    res.append("")
            else:
                res.append(s[i])
        for i in stack:
            res[i] = ""
        return "".join(res)


        


        
