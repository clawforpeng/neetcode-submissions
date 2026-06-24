class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        sol = 1

        substrings = defaultdict(bool)
        substrings[s[0]] = True

        left = 0
        right = 1

        current = 1

        # x y z z y
        while right < len(s):
            if substrings[s[right]] == False:
                substrings[s[right]] = True
                right += 1
                current += 1
                sol = max(sol, current)
            else:
                if s[left] != s[right]:
                    substrings[s[left]] = False
                    current -= 1  
                else:
                    right += 1
                left += 1        

        return sol