class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # sol = 0
        n = len(nums)
        memo = [{} for _ in range(n)]

        memo[0][nums[0]] = 1
        memo[0][-nums[0]] = 1 + memo[0].get(-nums[0], 0)

        for i in range(1, n):
            num = nums[i]
            for key, val in memo[i - 1].items():
                memo[i][key + num] = val + memo[i].get(key + num, 0)
                memo[i][key - num] = val + memo[i].get(key - num, 0)
        
        return memo[n - 1].get(target, 0)

        # 1 1 1
        # (1, -1) (2 0 0 -1) (3, )
        # def rec(i: int, acc: int) -> int:
        #     if i == n:
        #         if acc == target:
        #             return 1
        #         return 0
            
        #     num = nums[i]

        #     return rec(i + 1, acc + num) + rec(i + 1, acc - num)
                

        # return rec(0, 0)