class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sortedNums = sorted(nums)
        sols = []

        i = 0

        # -4 -1 -1 0 1 2; -1 -1 -1 0 0 1 1 2
        while i < len(sortedNums):
            while i + 2 < len(sortedNums) and sortedNums[i] == sortedNums[i + 2] and sortedNums[i] != 0:
                i += 1

            left = i + 1
            right = len(sortedNums) - 1

            while left < right:
                if sortedNums[i] + sortedNums[left] + sortedNums[right] == 0:
                    sols.append([sortedNums[i], sortedNums[left], sortedNums[right]])
                    left += 1
                    right -= 1
                    while left < right and sortedNums[left] == sortedNums[left - 1]:
                        left += 1
                    while left < right and sortedNums[right] == sortedNums[right + 1]:
                        right -= 1
                elif sortedNums[i] + sortedNums[left] + sortedNums[right] < 0:
                    left += 1
                else:
                    right -= 1
            
            i += 1
            if i < len(sortedNums) and sortedNums[i] == sortedNums[i - 1]:
                i += 1
        
        return sols

            