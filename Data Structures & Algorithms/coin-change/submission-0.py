class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # if amount == 0:
        #     return 0

        dp: List[int] = [-1] * (amount + 1)
        dp[amount] = 0
        
        for i in range(len(dp) - 1, -1, -1):
            if dp[i] == -1:
                continue

            for coin in coins:
                j = i - coin
                if j >= 0:
                    if dp[j] == -1:
                        dp[j] = 1 + dp[i]
                    else:
                        dp[j] = min(dp[i] + 1, dp[j])

        return dp[0]
