class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:

        # 0: untouched, 1: False, 2: True
        dp: List[int] = [0] * len(s)
        
        def rec(i: int) -> bool:
            string = s[i:]
            # if not string:
            #     return True
            if dp[i] == 2:
                return True
            if dp[i] == 1:
                return False
            sol = False
            for word in wordDict:
                if string.startswith(word):
                    if len(word) < len(string):
                        sol = sol or rec(i + len(word))
                        # if sol:
                        #     dp[i] = 2
                        #     return True
                    else:
                        dp[i] = 2
                        return True
            
            if sol:
                dp[i] = 2
            else:
                dp[i] = 1
            return sol
        
        return rec(0)