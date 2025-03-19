class Solution:
    def maxVowels(self, s: str, k: int) -> int:
        vowels = {'a', 'e', 'i', 'o', 'u'}
        curr = 0

        if len(s) == 1:
            return 1 if s[0] in vowels else 0

        for i in range(k):
            if s[i] in vowels:
                curr += 1
        max_vow = curr

        for i in range(1, len(s)-k +1):
            j = i + k -1
            if j < len(s):
                if s[i-1] in vowels:
                    curr -= 1
                if s[j] in vowels:
                    curr += 1
                max_vow = max(max_vow, curr)
        return max_vow

            

            
