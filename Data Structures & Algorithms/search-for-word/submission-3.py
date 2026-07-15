class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        for i in range(len(board)):
            for j in range(len(board[i])):
                visited = [[False for b in board[0]] for bo in board]
                ans = self.dfs(board, word, "", i, j, visited)
                if ans: return True
        return False

        
    def dfs(self, board: List[List[str]], word: str, cur: str, i: int, j: int, visited: List[List[bool]]) -> bool:
        if i < 0 or i >= len(board):
            return False
        
        if j < 0 or j >= len(board[0]):
            return False
        
        if visited[i][j]:
            return False

        tmp = cur + board[i][j]

        if tmp == word:
            return True
        
        if tmp != word[:len(tmp)]:
            return False
        
        visited[i][j] = True
        cur = tmp

        found = (
            self.dfs(board, word, tmp, i + 1, j, visited)
            or self.dfs(board, word, tmp, i - 1, j, visited)
            or self.dfs(board, word, tmp, i, j + 1, visited)
            or self.dfs(board, word, tmp, i, j - 1, visited)
        )

        visited[i][j] = False  # undo before returning to parent

        return found