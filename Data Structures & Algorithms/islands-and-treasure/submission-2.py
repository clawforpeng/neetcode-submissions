class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        queue = deque()
        m = len(grid)
        n = len(grid[0])
        inf = 2 ** 31 - 1
        visited = set()

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 0:
                    queue.append((i, j))
        
        distance = 0
        while queue:
            length = len(queue)

            for _ in range(length):
                cell = queue.popleft()
                i = cell[0]
                j = cell[1]
                grid[i][j] = distance
                if i - 1 >= 0 and grid[i - 1][j] == inf and (i - 1, j) not in visited:
                    queue.append((i - 1, j))
                    visited.add((i - 1, j))
                if i + 1 < m and grid[i + 1][j] == inf and (i + 1, j) not in visited:
                    queue.append((i + 1, j))
                    visited.add((i + 1, j))
                if j - 1 >= 0 and grid[i][j - 1] == inf and (i, j - 1) not in visited:
                    queue.append((i, j - 1))
                    visited.add((i, j - 1))
                if j + 1 < n and grid[i][j + 1] == inf and (i, j + 1) not in visited:
                    queue.append((i, j + 1))
                    visited.add((i, j + 1))
            
            distance += 1