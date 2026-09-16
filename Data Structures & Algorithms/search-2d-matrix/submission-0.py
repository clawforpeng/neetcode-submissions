class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])

        start = 0
        end = m - 1

        while start <= end:
            mid = (start + end) // 2
            row = matrix[mid]

            if row[-1] < target:
                start = mid + 1
            elif row[0] > target:
                end = mid - 1
            else:
                break

        if start > end:
            return False
        
        row = matrix[(start + end) // 2]

        left = 0
        right = n - 1

        while left <= right:
            mid = (left + right) // 2
            if target > row[mid]:
                left = mid + 1
            elif target < row[mid]:
                right = mid - 1
            else:
                return True
        
        return False
