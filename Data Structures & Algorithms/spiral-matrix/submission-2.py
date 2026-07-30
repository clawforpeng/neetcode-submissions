class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        sols = []
        n, m = len(matrix), len(matrix[0])

        top, left = 0, 0
        bottom, right = n - 1, m - 1

        while top <= bottom and left <= right:
            # Only one row remains
            if top == bottom:
                sols.extend(matrix[top][left:right + 1])
                break

            # Only one column remains
            if left == right:
                for i in range(top, bottom + 1):
                    sols.append(matrix[i][left])
                break

            # Top row, excluding the top-right corner
            sols.extend(matrix[top][left:right])

            # Right column, excluding the bottom-right corner
            for i in range(top, bottom):
                sols.append(matrix[i][right])

            # Bottom row, excluding the bottom-left corner
            for i in range(right, left, -1):
                sols.append(matrix[bottom][i])

            # Left column, excluding the top-left corner
            for i in range(bottom, top, -1):
                sols.append(matrix[i][left])

            top += 1
            bottom -= 1
            left += 1
            right -= 1

        return sols