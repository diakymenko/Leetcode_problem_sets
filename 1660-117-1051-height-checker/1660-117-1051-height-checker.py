class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        lst_sorted = sorted(heights)
        count = 0

        for i in range(len(heights)):
            if heights[i] != lst_sorted[i]:
                count += 1
        return count

        
            