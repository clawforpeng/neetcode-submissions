class Solution:
    def countSubstrings(self, s: str) -> int:
        dp = [[False] * len(s) for _ in range(len(s))]
        count = 0

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                    count += 1
                elif i + 1 == j:
                    if s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = False
                else:
                    if dp[i + 1][j - 1] and s[i] == s[j]:
                        dp[i][j] = True
                        count += 1
                    else:
                        dp[i][j] = False
        
        return count