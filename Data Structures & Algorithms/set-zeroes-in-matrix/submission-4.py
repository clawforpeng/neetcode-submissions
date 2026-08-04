class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        isRowZeroZero = False

        for r in range(0, len(matrix)):
            for c in range(len(matrix[0])):
                if matrix[r][c] == 0:
                    matrix[0][c] = 0
                    if r != 0:
                        matrix[r][0] = 0
                    else:
                        isRowZeroZero = True
        
        for r in range(1, len(matrix)):
            if matrix[r][0] == 0:
                matrix[r] = [0] * len(matrix[0])
        
        for c in range(len(matrix[0])):
            if matrix[0][c] == 0:
                for r in range(len(matrix)):
                    matrix[r][c] = 0
        
        if isRowZeroZero:
            matrix[0] = [0] * len(matrix[0])
        