class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for char in s:
            if char != ']':
                stack.append(char)
            else:
                temp_str = ""
                while stack[-1] != '[':
                    temp_str = stack.pop() + temp_str
                stack.pop()
                num = ""
                while stack and stack[-1].isdigit():
                    num = stack.pop() + num
                temp_str = int(num) * temp_str
                stack.append(temp_str)
        return "".join(stack)


                    