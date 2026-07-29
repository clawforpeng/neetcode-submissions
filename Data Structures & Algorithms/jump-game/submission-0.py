class Solution:
    def canJump(self, nums: List[int]) -> bool:
        dp: List[bool] = [False] * len(nums)

        dp[-1] = True

        for i in range(len(nums) - 2, -1, -1):
            jumps = nums[i]

            for j in range(i + 1, i + jumps + 1):
                if j == len(nums) - 1:
                    dp[i] = True
                    break
                
                if dp[j]:
                    dp[i] = True
                    break
            
        return dp[0]