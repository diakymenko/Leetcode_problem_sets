class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_s = {}
        for letter in s:
            dict_s.setdefault(letter,0)
            dict_s[letter] += 1
        
        for letter in t:
            if letter in dict_s:
                dict_s[letter] -= 1
                if  dict_s[letter] == 0:
                    del dict_s[letter]
            else:
                return False
        
        if len(dict_s) != 0:
            return False
        return True