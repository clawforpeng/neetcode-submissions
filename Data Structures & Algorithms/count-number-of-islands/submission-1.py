class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        sol = 0
        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
                return
            if grid[i][j] != "1":
                return
            grid[i][j] = "-1"

            dfs(i + 1, j)
            dfs(i - 1, j)
            dfs(i, j + 1)
            dfs(i, j - 1)

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == "1":
                    dfs(i, j)
                    sol += 1
        
        return sol
