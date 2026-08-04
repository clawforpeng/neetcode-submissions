class Solution:
    def countBits(self, n: int) -> List[int]:
        sols = []

        for i in range(n + 1):
            sol = 0
            while i:
                sol += i & 1
                i = i >> 1
            sols.append(sol)
        
        return sols