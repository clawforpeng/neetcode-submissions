class Solution:
    def validPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1

        def search(i: int, j: int, extra: bool) -> bool:
            if i >= j:
                return True
            
            if s[i] == s[j]:
                i += 1
                j -= 1
                return search(i, j, extra)
            else:
                if not extra:
                    return False
                return search(i + 1, j, False) or search(i, j - 1, False)
        
        return search(left, right, True)