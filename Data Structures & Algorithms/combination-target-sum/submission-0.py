class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        ans = []
        sortedN = sorted(nums)

        def dfs(choices: List[int], sum: int, index: int):
            if index == len(sortedN):
                return
            
            val = sortedN[index]
            if sum + val == target:
                newChoices = list(choices)
                newChoices.append(val)
                ans.append(newChoices)
            elif sum + val > target:
                return
            else:
                newChoices = list(choices)
                newChoices.append(val)
                dfs(newChoices, sum + val, index)
                newChoices.pop()
                dfs(newChoices, sum, index + 1)

        dfs([], 0, 0)
        return ans
