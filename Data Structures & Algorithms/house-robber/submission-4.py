class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        maxRob: List[int] = [0 for _ in range(len(nums))]
        maxRob[0] = nums[0]
        maxRob[1] = max(nums[0], nums[1])
        for i in range(2, len(nums)):
            maxRob[i] = max(maxRob[i - 2] + nums[i], maxRob[i - 1])
        
        return max(maxRob[len(nums) - 1], maxRob[len(nums) - 2])
