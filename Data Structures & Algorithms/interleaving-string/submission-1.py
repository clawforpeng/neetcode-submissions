class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False
        

        dp = [[0] * (len(s2) + 1)  for _ in range(len(s1) + 1)]

        def rec(i: int, j: int) -> bool:
            if i == len(s1) and j == len(s2):
                return True
            
            if dp[i][j] != 0:
                return dp[i][j] == 1

            if i < len(s1) and s1[i] == s3[i + j]:
                if rec(i + 1, j):
                    dp[i][j] = 1
                    return True
            
            if j < len(s2) and s2[j] == s3[i + j]:
                if rec(i, j + 1):
                    dp[i][j] = 1
                    return True
            
            dp[i][j] = -1
            return False
        
        return rec(0, 0)