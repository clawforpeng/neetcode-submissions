class Solution:
    def solve(self, board: List[List[str]]) -> None:
        m = len(board)
        n = len(board[0])

        def dfs(i: int, j: int):
            if i < 0 or j < 0 or i == m or j == n:
                return
            if board[i][j] == "O":
                board[i][j] = "T"
                dfs(i - 1, j)
                dfs(i + 1, j)
                dfs(i, j - 1)
                dfs(i, j + 1)

        for i in range(n):
            if board[0][i] == "O":
                dfs(0, i)
            if board[m - 1][i] == "O":
                dfs(m - 1, i)
        
        for i in range(m):
            if board[i][0] == "O":
                dfs(i, 0)
            if board[i][n - 1] == "O":
                dfs(i, n - 1)
        
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "T":
                    board[i][j] = "O"