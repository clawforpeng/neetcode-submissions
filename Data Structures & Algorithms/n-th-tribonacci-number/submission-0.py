class Solution:
    def tribonacci(self, n: int) -> int:
        t0 = 0
        t1 = 1
        t2 = 1

        if n == 0:
            return t0
        if n == 1:
            return t1
        if n == 2:
            return t2

        for _ in range(n - 2):
            total = t0 + t1 + t2
            t0 = t1
            t1 = t2
            t2 = total
        
        return t2