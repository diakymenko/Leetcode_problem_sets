class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:

        # chars = {}
        
        # for word in strs:
        #     key = tuple(sorted(word))
        #     chars.setdefault(key, [])
        #     chars[key].append(word)
        # res = []

        # for key,val in chars.items():
        #     res.append(val)
        # return res

        
        # count of characters as key in a dictionary, list of words as the value
        words = defaultdict(list)
        for word in strs:
            hashed_word = {char: 0 for char in "abcdefghijklmnopqrstuvwxyz"}
            for char in word:
                hashed_word[char] += 1
            words[(tuple(hashed_word.items()))].append(word)

            
        return list(words.values())

        # Time: O(NK) where N is the length of strs and K is the max len of a string in strs
        # Space: O(NK)

            
