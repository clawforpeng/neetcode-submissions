class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ans = nums[0]
        cur = ans

        j = 1

        while j < len(nums):
            num = nums[j]

            if num > cur:
                if cur < 0:
                    cur = num
                    j += 1
                else:
                    cur += num
                    j += 1
            else:
                cur += num
                j += 1
            
            ans = max(ans, cur)
        
        return ans
            