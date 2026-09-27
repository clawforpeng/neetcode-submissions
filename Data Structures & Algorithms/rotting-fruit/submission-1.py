class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        visited = set()

        m = len(grid)
        n = len(grid[0])
        sol = -1
        fresh = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    queue.append((i, j))
                if grid[i][j] == 1:
                    fresh += 1
        
        while queue:
            length = len(queue)
            sol += 1

            for _ in range(length):
                fruit = queue.popleft()
                i = fruit[0]
                j = fruit[1]

                if i + 1 < m and (i + 1, j) not in visited and grid[i + 1][j] == 1:
                    grid[i + 1][j] = -1
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                    fresh -= 1
                if i - 1 >= 0 and (i - 1, j) not in visited and grid[i - 1][j] == 1:
                    grid[i - 1][j] = -1
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))
                    fresh -= 1
                if j + 1 < n and (i, j + 1) not in visited and grid[i][j + 1] == 1:
                    grid[i][j + 1] = -1
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
                    fresh -= 1
                if j - 1 >= 0 and (i, j - 1) not in visited and grid[i][j - 1] == 1:
                    grid[i][j - 1] = -1
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))
                    fresh -= 1
        
        if fresh > 0:
            return -1
        if sol == -1:
            return 0
        return sol

