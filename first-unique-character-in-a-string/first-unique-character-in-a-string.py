class Solution:
    def firstUniqChar(self, s: str) -> int:

        seen = set()
        hashmap = {}


        for idx, char in enumerate(s):
            if char not in seen:
                hashmap[char] = idx
                seen.add(char)
            elif char in hashmap:
                del hashmap[char]
        
        return min(hashmap.values()) if hashmap else -1
