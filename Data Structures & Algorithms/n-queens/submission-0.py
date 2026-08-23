class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        sols = []

        def rec(cols: List[int], i: int):
            if i == n:
                sol = []
                for r in range(n):
                    chessrow = ""
                    pos = cols[r]
                    for c in range(n):
                        if c == pos:
                            chessrow += "Q"
                        else:
                            chessrow += "."
                    sol.append(chessrow)
                sols.append(sol)
            else:
                for c in range(n):
                    if c in cols:
                        continue
                    posDiagnol = c + i
                    negDiagnol = c - i

                    isValid = True
                    for row, col in enumerate(cols):
                        if col + row == posDiagnol:
                            isValid = False
                        elif col - row == negDiagnol:
                            isValid = False
                    
                    if isValid:
                        cols.append(c)
                        rec(cols, i + 1)
                        cols.remove(c)
        

        rec([], 0)

        return sols