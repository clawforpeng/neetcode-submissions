class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        sols = []
        nums.sort() # 1 1 2

        def rec(i: int, acc: List[int]):
            if i == len(nums):
                sols.append(list(acc))
                return
            
            # sols.append(list(acc))
            acc.append(nums[i])
            rec(i + 1, acc)
            acc.pop()

            while i + 1 < len(nums) and nums[i] == nums[i + 1]:
                i += 1
            rec(i + 1, acc)
        
        rec(0, [])

        return sols

            
