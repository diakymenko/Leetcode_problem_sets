class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # for i in range(len(numbers)):
        #     num = target - numbers[i]
        #     start = i
        #     end = len(numbers) - 1
        #     while start <= end:
        #         mid = (start + end) // 2
        #         if numbers[mid] == num and i != mid:
        #             return [i+1, mid+1]
        #         elif numbers[mid] > num:
        #             end = mid -1
        #         else:
        #             start = mid + 1

        start = 0
        end = len(numbers) -1

        while start <= end:
            if numbers[start] + numbers[end] == target and start != end:
                return [start +1, end +1]
            elif numbers[start] + numbers[end] > target:
                end-=1
            else:
                start += 1
         
        

        