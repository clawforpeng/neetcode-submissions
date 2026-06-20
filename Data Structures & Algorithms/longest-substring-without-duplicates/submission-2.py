class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) < 2:
            return len(s)

        maxLength, length = 1, 1
        i = 0
        j = 1

        hashmap = defaultdict(bool)
        hashmap[s[i]] = True

        while j < len(s):
            if hashmap[s[j]] == False:
                hashmap[s[j]] = True
                length += 1
                j += 1
                maxLength = max(length, maxLength)
            else:
                hashmap[s[i]] = False
                length -= 1
                i += 1
        
        return maxLength
