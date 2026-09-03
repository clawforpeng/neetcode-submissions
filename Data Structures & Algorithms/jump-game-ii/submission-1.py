class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = [-1] * len(nums)
        memo[-1] = 0

        def rec(i: int) -> int:
            # if i >= len(nums):
            #     return -1
            # if i == len(nums) - 1:
            #     return 0
            if memo[i] != -1:
                return memo[i]

            sol = 1001
            for j in range(1, nums[i] + 1):
                if i + j >= len(nums):
                    break
                sol = min(sol, rec(i + j))

            memo[i] = sol + 1
            return memo[i]

        return rec(0)
            