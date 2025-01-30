class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        lst1 = list(s)
        lst1.sort()
        lst2 = list(t)
        lst2.sort()
        return lst2 == lst1
    
