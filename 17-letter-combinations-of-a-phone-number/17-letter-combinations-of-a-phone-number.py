class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        dict_ = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }
        
        res = []
        lst_digits = list(digits)
        
        if len(lst_digits) >= 1:
            for i in range(len(dict_[int(lst_digits[0])])):
                if len(lst_digits) == 1:
                    res.append(f"{dict_[int(lst_digits[0])][i]}")
                elif len(lst_digits) == 2:
                    for j in range(len(dict_[int(lst_digits[1])])):
                        res.append(f"{dict_[int(lst_digits[0])][i]}{dict_[int(lst_digits[1])][j]}")
                elif len(lst_digits) == 3:
                    for j in range(len(dict_[int(lst_digits[1])])):
                        for y in range(len(dict_[int(lst_digits[2])])):
                            res.append(f"{dict_[int(lst_digits[0])][i]}{dict_[int(lst_digits[1])][j]}{dict_[int(lst_digits[2])][y]}")
                elif len(lst_digits) == 4:
                    for j in range(len(dict_[int(lst_digits[1])])):
                        for y in range(len(dict_[int(lst_digits[2])])):
                            for x in range(len(dict_[int(lst_digits[3])])):
                                res.append(f"{dict_[int(lst_digits[0])][i]}{dict_[int(lst_digits[1])][j]}{dict_[int(lst_digits[2])][y]}{dict_[int(lst_digits[3])][x]}")
                    
        return res