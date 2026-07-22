class Solution:
    def climbStairs(self, n: int) -> int:
        ways = [0 for _ in range(n + 1)]
        ways[0] = 1
        ways[1] = 1

        i = 2
        while i < len(ways):
            ways[i] = ways[i - 1] + ways[i - 2]
            i += 1
        
        return ways[n]