class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        max_num = sum(weights)
        min_num = max(weights)

        def count_days(mid, weights):
            temp_sum = 0
            days = 1
            for i in range(len(weights)):
                if temp_sum + weights[i] > mid:
                    days+= 1
                    temp_sum = weights[i]
                elif temp_sum + weights[i] == mid:
                    temp_sum = 0
                    if i != len(weights) -1:
                        days += 1
                else:
                    temp_sum += weights[i]
            return days



        while min_num <= max_num:
            mid = (min_num + max_num) // 2
            num_days = count_days(mid, weights)
            if num_days > days:
                min_num = mid + 1
            else:
                max_num = mid - 1
        return min_num


