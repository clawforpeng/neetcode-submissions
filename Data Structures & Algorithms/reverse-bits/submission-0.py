class Solution:
    def reverseBits(self, n: int) -> int:
        sol = 0
        for i in range(32):
            cur = n & 1

            cur = cur << (31 - i)
            sol = sol | cur

            n = n >> 1
        
        return sol