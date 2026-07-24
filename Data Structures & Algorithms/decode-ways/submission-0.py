class Solution:
    def numDecodings(self, s: str) -> int:
        # index represents the substring starting index
        dp: List[int] = [0] * len(s)
        dp[len(s) - 1] = 1 if int(s[len(s) - 1]) > 0 else 0

        for i in range(len(s) - 2, -1, -1):
            ans = 0
            # single digit
            single = int(s[i])
            if single > 0:
                ans = dp[i + 1]

            # double digits
            double = int(s[i : i + 2])
            if double >= 10 and double <= 26:
                if i + 2 == len(s):
                    ans += 1
                else:
                    ans += dp[i + 2]
            
            dp[i] = ans
        
        return dp[0]
            
            
            # 123

            # 3
            # -----
            # 2 3

            # 23
            # ----

            # 1 -> (2 3, 23)
            # 12 -> (3)
        
