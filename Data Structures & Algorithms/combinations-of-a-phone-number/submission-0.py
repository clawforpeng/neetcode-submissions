class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        sols = []

        if not digits:
            return sols

        dicts = {}

        dicts["2"] = ["a", "b", "c"]
        dicts["3"] = ["d", "e", "f"]
        dicts["4"] = ["g", "h", "i"]
        dicts["5"] = ["j", "k", "l"]
        dicts["6"] = ["m", "n", "o"]
        dicts["7"] = ["p", "q", "r", "s"]
        dicts["8"] = ["t", "u", "v"]
        dicts["9"] = ["w", "x", "y", "z"]

        def rec(i: int, acc: List[str]):
            if i == len(digits):
                sols.append("".join(acc))
                return
            
            digit = digits[i]
            chars = dicts[digit]

            for c in chars:
                acc.append(c)
                rec(i + 1, acc)
                acc.pop()
        
        rec(0, [])

        return sols
                
