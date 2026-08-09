class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 4 + 7
        # 100
        # 111 7
        # 101 5
      #  1000

        sol = 0
        advance = False

        for pos in range(32):
            aBit = a & 1
            bBit = b & 1

            if aBit == 1 and bBit == 1:
                if advance:
                    sol = (1 << pos) | sol
                advance = True
            elif aBit == 0 and bBit == 0:
                if advance:
                    sol = (1 << pos) | sol
                advance = False
            else:
                if advance:
                    advance = True
                else:
                    sol = (1 << pos) | sol
                    advance = False
            a = a >> 1
            b = b >> 1
        
        # if advance:
        #     sol = (1 << pos) | sol
        
        if sol > 0x7FFFFFFF:
            sol = ~(sol ^ 0xFFFFFFFF)
        
        return sol
