class Solution:
    def compressedString(self, word: str) -> str:
        res = []
        char = word[0]
        count = 1

        for i in range(1, len(word)):
            if char == word[i] and count < 9:
                count += 1
            else:
                res.append(str(count))
                res.append(char)
                char = word[i]
                count = 1
        res.append(str(count))
        res.append(char)

        return "".join(res)
            
            