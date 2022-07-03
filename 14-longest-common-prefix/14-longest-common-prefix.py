class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
#         prefix = strs[0]
    
#         for word in strs:
#             if not word:
#                 return ""
#             min_word = min(word, prefix)
#             for i in range(len(min_word)):
#                 if word[i] != prefix[i]:
#                     prefix = prefix[0:i]
#                     break
#                 elif word[i] == prefix[i] and i == len(min_word) -1:
#                     prefix = min_word
#         return prefix

        if not strs:
            return ""
        shortest = min(strs, key=len)
        for i, ch in enumerate(shortest):
            for other in strs:
                if other[i] != ch:
                    return shortest[:i]
        return shortest

            