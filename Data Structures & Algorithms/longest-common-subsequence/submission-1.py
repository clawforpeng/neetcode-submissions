class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        dp: List[List[int]] = [[-1] * len(text2) for _ in range(len(text1))]

        def longest(i: int, j: int) -> int:
            if i == len(text1) or j == len(text2):
                return 0
            
            if dp[i][j] != -1:
                return dp[i][j]

            sol = 0

            char1, char2 = text1[i], text2[j]

            if char1 == char2:
                sol = 1 + longest(i + 1, j + 1)
            
            sol = max(longest(i, j + 1), sol, longest(i + 1, j))

            dp[i][j] = sol
            return sol
        
        return longest(0, 0)