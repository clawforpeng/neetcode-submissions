class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        firstNums = {}

        for idx, num in enumerate(nums):
            if num in firstNums:
                if idx - firstNums[num] <= k:
                    return True
                else:
                    firstNums[num] = idx
            else:
                firstNums[num] = idx
        
        return False