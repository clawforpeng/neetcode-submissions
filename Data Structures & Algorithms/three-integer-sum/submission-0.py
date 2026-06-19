class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sols = []
        sortedNums = sorted(list(nums))

        i = 0

        while i < len(sortedNums) - 2:
            if i > 0 and sortedNums[i] == sortedNums[i - 1]:
                i += 1
                continue
            
            target = 0 - sortedNums[i]
            j = i + 1
            k = len(sortedNums) - 1

            while j < k:
                sum = sortedNums[j] + sortedNums[k]                 
                
                if sum == target:
                    sols.append([sortedNums[i], sortedNums[j], sortedNums[k]])
                    while j < k and sortedNums[j] == sortedNums[j + 1]:
                        j += 1
                    while j < k and sortedNums[k] == sortedNums[k - 1]:
                        k -= 1
                    j += 1
                    k -= 1
                elif sum > target:
                    k -= 1
                else:
                    j += 1
            
            i += 1
        
        return sols