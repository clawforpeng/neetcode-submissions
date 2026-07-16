class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        visited = [[False for _ in grid[0]] for _ in grid]
        sol = 0

        def searchIsland(i: int, j: int, hasIsland: bool):
            nonlocal sol
            if i < 0 or i >= len(grid):
                return
            if j < 0 or j >= len(grid[i]):
                return
            if visited[i][j] or grid[i][j] == "0":
                return
            # unvisited and grid[i][j] is 1
            visited[i][j] = True

            if not hasIsland:
                sol += 1

            searchIsland(i + 1, j, True)
            searchIsland(i - 1, j, True)
            searchIsland(i, j + 1, True)
            searchIsland(i, j - 1, True)
        
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                searchIsland(i, j, False)

        return sol
