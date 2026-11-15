class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        total = sum(piles)
        memo = {}

        def rec(alice: bool, i: int, j: int) -> int:
            if i > j:
                return 0
            
            if (alice, i, j) in memo:
                return memo[(alice, i, j)]
            
            sol = 0
            if alice:
                sol = max(piles[i] + rec(not alice, i + 1, j), piles[j] + rec(not alice, i , j - 1))
                memo[(alice, i, j)] = sol
                return sol
            else:
                sol = min(rec(not alice, i + 1, j), rec(not alice, i, j - 1))
                memo[(alice, i, j)] = sol
                return sol
        
        score = rec(True, 0, len(piles) - 1)
        
        return score > total - score