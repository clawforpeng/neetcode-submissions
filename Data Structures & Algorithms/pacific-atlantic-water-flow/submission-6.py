class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        sols = []

        canPacific = [[False for _ in heights[0]] for _ in heights]
        canAtlantic = [[False for _ in heights[0]] for _ in heights]

        for i in range(len(heights[0])):
            canPacific[0][i] = True
            canAtlantic[len(heights) - 1][i] = True
        
        for r in range(len(heights)):
            canPacific[r][0] = True
            canAtlantic[r][len(heights[0]) - 1] = True
        
        def dfs(r: int, c: int, canVisited: List[List[bool]]):
            if r < len(canVisited) - 1:
                if not canVisited[r + 1][c]:
                    if heights[r + 1][c] >= heights[r][c]:
                        canVisited[r + 1][c] = True
                        dfs(r + 1, c, canVisited)
            
            if r > 0:
                if not canVisited[r - 1][c]:
                    if heights[r - 1][c] >= heights[r][c]:
                        canVisited[r - 1][c] = True
                        dfs(r - 1, c, canVisited)
            
            if c < len(canVisited[0]) - 1:
                if not canVisited[r][c + 1]:
                    if heights[r][c + 1] >= heights[r][c]:
                        canVisited[r][c + 1] = True
                        dfs(r, c + 1, canVisited)

            if c > 0:
                if not canVisited[r][c - 1]:
                    if heights[r][c - 1] >= heights[r][c]:
                        canVisited[r][c - 1] = True
                        dfs(r, c - 1, canVisited)

        for i in range(len(heights[0])):
            dfs(0, i, canPacific)
            dfs(len(heights) - 1, i, canAtlantic)
        
        for r in range(len(heights)):
            dfs(r, 0, canPacific)
            dfs(r, len(heights[0]) - 1, canAtlantic)

        for i in range(len(heights)):
            for j in range(len(heights[0])):
                if canPacific[i][j] and canAtlantic[i][j]:
                    sols.append([i, j])

        return sols