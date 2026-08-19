class Solution:
    def reverse(self, x: int) -> int:
        sol = 0
        isNegative = True if x < 0 else False
        num = abs(x)

        while num:
            remainder = num % 10
            sol = sol * 10 + remainder

            num = num // 10
        
        if isNegative:
            sol = sol * -1
        
        if sol < (-2 ** 31) or sol > (2 ** 31 - 1):
            return 0

        return sol