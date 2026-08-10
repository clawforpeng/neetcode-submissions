class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        matrix.reverse()

        for i in range(len(matrix)):
            for j in range(i + 1, len(matrix)):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


        # 7 8 9
        # 4 5 6
        # 1 2 3