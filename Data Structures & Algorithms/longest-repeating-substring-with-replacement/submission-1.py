class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        right = 0

        tracker = defaultdict(int)
        maxLength = 0
        maxChar = s[0]

        while right < len(s):
            tracker[s[right]] += 1
            length = right - left + 1

            if length <= k + tracker[s[right]]:
                maxChar = s[right]
                maxLength = max(maxLength, length)
            else:
                if length > tracker[maxChar] + k:
                    tracker[s[left]] -= 1
                    left += 1
                else:
                    maxLength = max(maxLength, length)
            
            right += 1
        
        return maxLength