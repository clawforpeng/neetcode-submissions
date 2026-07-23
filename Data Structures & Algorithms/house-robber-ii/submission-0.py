class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]
        
        if len(nums) == 2:
            return max(nums[0], nums[1])
        
        noHead = nums[1:]
        noTail = nums[: -1]

        noHeadMax = [0 for _ in noHead]
        noTailMax = [0 for _ in noTail]

        noHeadMax[0] = noHead[0]
        noTailMax[0] = noTail[0]

        noHeadMax[1] = max(noHeadMax[0], noHead[1])
        noTailMax[1] = max(noTailMax[0], noTail[1])

        for i in range(2, len(noHead)):
            noHeadMax[i] = max(noHeadMax[i - 1], noHeadMax[i - 2] + noHead[i])
            noTailMax[i] = max(noTailMax[i - 1], noTailMax[i - 2] + noTail[i])
        
        return max(noHeadMax[-1], noTailMax[-1])