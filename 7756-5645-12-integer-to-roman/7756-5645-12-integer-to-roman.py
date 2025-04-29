class Solution:
    def intToRoman(self, num: int) -> str:
        book = {
        1: 'I', 
        5: 'V', 
        10: 'X', 
        50: 'L', 
        100: 'C', 
        500: 'D', 
        1000: 'M'
        }
        
        lst = []

        while num:
            lst.append(num%10)
            num = num //10
        lst_rome = []
        temp = 1

        for num in lst:
            if num == 4 or num == 9:
                first = book[temp]
                if num == 4:
                    second = book[temp * 5]
                elif num == 9:
                    second = book[temp * 10]
                lst_rome.append(first + second)
            elif num * temp in book:
                lst_rome.append(book[num*temp])
            elif 6 <= num <= 8:
                first = book[temp * 5]
                second = ""
                remainder = num - 5
                for i in range(remainder):
                    second += book[1 * temp]
                lst_rome.append(first+second)
            else:
                first = ""
                for i in range(num):
                    first += book[temp]
                lst_rome.append(first)
            temp *=10
        
        return "".join(lst_rome[::-1])
        



        



