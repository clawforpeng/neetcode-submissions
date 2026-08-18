class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        maxArea = 0

        m = len(grid)
        n = len(grid[0])

        visited = [[False] * n for _ in range(m)]

        def rec(r: int, c: int) -> int:
            nonlocal maxArea
            if r == m or c == n or r < 0 or c < 0:
                return 0
            if visited[r][c]:
                return 0
            visited[r][c] = True

            if not grid[r][c]:
                # rec(r + 1, c)
                # rec(r, c + 1)
                return 0
            
            area = 1 + rec(r + 1, c) + rec(r - 1, c) + rec(r, c + 1) + rec(r, c - 1)
            maxArea = max(area, maxArea)
            return area

        for i in range(m):
            for j in range(n):
                rec(i, j)

        return maxArea