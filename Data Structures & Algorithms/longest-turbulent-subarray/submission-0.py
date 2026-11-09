class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        memo = [[-1, 0] for _ in range(len(arr))] # first is to indicate the end index, second is to indicate greater 1, less -1, and equal 0 to the next ele

        for i in range(len(arr) - 2, -1, -1):
            right = arr[i + 1]
            cur = arr[i]

            if cur == right:
                continue
            
            if cur < right:
                memo[i][1] = -1

                if memo[i + 1][1] == 1:
                    memo[i][0] = memo[i + 1][0]
                    
                else:
                    memo[i][0] = i + 1
                    
            else:
                memo[i][1] = 1

                if memo[i + 1][1] == -1:
                    memo[i][0] = memo[i + 1][0]
                    
                else:
                    memo[i][0] = i + 1
                    
        
        sol = 1

        for i in range(len(memo)):
            if memo[i][0] != -1:
                sol = max(sol, memo[i][0] - i + 1)

        return sol