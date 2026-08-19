class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        m = len(word1)
        n = len(word2)

        memo = [[-1] * n for _ in range(m)]

        def rec(i: int, j: int) -> int:
            if i == m:
                return n - j
            if j == n:
                return m - i
            
            if memo[i][j] != -1:
                return memo[i][j]
            
            if word1[i] == word2[j]:
                memo[i][j] = rec(i + 1, j + 1)
                return memo[i][j]
            
            sol = 1 + min(rec(i, j + 1), rec(i + 1, j), rec(i + 1, j + 1))
            memo[i][j] = sol
            return sol
        
        return rec(0, 0)