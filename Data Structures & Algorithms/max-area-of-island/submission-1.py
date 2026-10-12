class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        
        def dfs(i: int, j: int) -> int:
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return 0
            if grid[i][j] != 1:
                return 0
            
            sol = 1

            grid[i][j] = -1
            sol += dfs(i + 1, j)
            sol += dfs(i - 1, j)
            sol += dfs(i, j + 1)
            sol += dfs(i, j - 1)

            return sol
        
        sol = 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    sol = max(sol, dfs(i, j))
        
        return sol