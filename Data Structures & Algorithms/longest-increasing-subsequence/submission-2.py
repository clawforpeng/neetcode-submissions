class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        dp: List[List[int]] = [[-1001] * (len(nums) + 1) for _ in range(len(nums) + 1)]
        
        # dp[0][0] = 1

        def LIS(prev: int, i: int) -> int:
            if i == len(nums):
                return 0
            
            if dp[prev + 1][i] != -1001:
                return dp[prev + 1][i]
            
            num = nums[i]
            sol = LIS(prev, i + 1)

            if prev == -1:
                    sol = max(sol, 1 + LIS(i, i + 1))
            else:
                if nums[prev] < num:
                    sol = max(sol, 1 + LIS(i, i + 1))

            dp[prev + 1][i] = sol
            return sol
        
        return LIS(-1, 0)