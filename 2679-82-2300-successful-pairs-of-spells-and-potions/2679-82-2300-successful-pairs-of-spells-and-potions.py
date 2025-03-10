class Solution:
    def successfulPairs(self, spells: List[int], potions: List[int], success: int) -> List[int]:
        res = []
        potions.sort()

        for i in range(len(spells)):
            count = 0
            start = 0
            end = len(potions) - 1
            spell_num = spells[i]
            rem = success%spell_num
            num = success // spell_num
            if rem != 0:
                num = success // spell_num + 1
            while start <= end:
                mid = (start + end) // 2
                if potions[mid] < num:
                    start = mid + 1
                else:
                    end = mid-1
            count = len(potions) - start
            res.append(count)

        return res
