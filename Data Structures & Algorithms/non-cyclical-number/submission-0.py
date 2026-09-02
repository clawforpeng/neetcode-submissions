class Solution:
    def isHappy(self, n: int) -> bool:

        visited = set()
        cur = n

        while True:
            chars = list(str(cur))
            total = 0
            for char in chars:
                digit = int(char)
                total += digit ** 2
            
            if total == 1:
                return True
            if total in visited:
                return False
            visited.add(total)
            cur = total
        