class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        dp: List[List[int]] = [[0] * len(nums) for _ in range(len(nums))]
        ans = -11

        for i in range(len(nums) - 1, -1, -1):
            for j in range(i, len(nums)):
                if i == j:
                    dp[i][j] = nums[i]
                else:
                    dp[i][j] = nums[i] * dp[i + 1][j]
                ans = max(ans, dp[i][j])
        
        return ans