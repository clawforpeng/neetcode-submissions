class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        maxDp: List[int] = [-10] * len(nums)
        minDp: List[int] = [10] * len(nums)

        maxDp[-1] = nums[-1]
        minDp[-1] = nums[-1]

        ans = nums[-1]

        for i in range(len(nums) - 2, -1, -1):
            num = nums[i]

            if num == 0:
                maxDp[i] = 0
                minDp[i] = 0
            else:
                maxDp[i] = max(num, maxDp[i + 1] * num, minDp[i + 1] * num)
                minDp[i] = min(num, maxDp[i + 1] * num, minDp[i + 1] * num)
            
            ans = max(ans, maxDp[i])
        
        return ans