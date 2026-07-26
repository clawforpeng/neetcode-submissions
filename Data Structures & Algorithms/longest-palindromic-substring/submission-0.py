class Solution:
    def longestPalindrome(self, s: str) -> str:
        dp: List[List[bool]] = [[False] * len(s) for _ in range(len(s))]
        ans = ""

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = True
                elif i + 1 == j:
                    dp[i][j] = s[i] == s[j]
                else:
                    dp[i][j] = dp[i + 1][j - 1] and s[i] == s[j]
        
                if dp[i][j] and j - i + 1 > len(ans):
                    ans = s[i : j + 1]
        
        return ans