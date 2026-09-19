class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sols = []

        def rec(i: int, acc: List[int]):
            if i == len(nums):
                sols.append(acc)
                return
            rec(i + 1, acc)
            newAcc = list(acc)
            newAcc.append(nums[i])
            rec(i + 1, newAcc)
        
        rec(0, [])

        return sols