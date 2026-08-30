class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for row in board:
            nums = set()

            for num in row:
                if num in nums:
                    return False
                if num != ".":
                    nums.add(num)
            
        for c in range(len(board[0])):
            nums = set()
            for r in range(len(board)):
                num = board[r][c]

                if num in nums:
                    return False
                if num != ".":
                    nums.add(num)

        r = 0
        c = 0

        for r in range(0, 9, 3):
            for c in range(0, 9, 3):
                nums = set()
                for i in range(r, r + 3):
                    for j in range(c, c + 3):
                        num = board[i][j]

                        if num in nums:
                            return False
                        if num != ".":
                            nums.add(num)
        
        return True

                