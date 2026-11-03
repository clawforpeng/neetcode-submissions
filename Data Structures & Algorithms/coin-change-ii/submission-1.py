class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        memo = [[-1] * len(coins) for _ in range(amount + 1)]

        def rec(amount: int, i: int) -> int:
            if memo[amount][i] != -1:
                return memo[amount][i]
            if amount == 0:
                memo[amount][i] = 1
                return 1
            if amount < 0:
                memo[amount][i] = 0
                return 0
            sol = 0
            for coin in range(i, len(coins)):
                sol += rec(amount - coins[coin], coin)
            memo[amount][i] = sol
            return sol
        
        return rec(amount, 0)