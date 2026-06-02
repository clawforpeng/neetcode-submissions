class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sDict = {}
        # tDict = {}
        for c in s:
            if c in sDict:
                sDict[c] += 1
            else:
                sDict[c] = 1
        for c in t:
            if c in sDict:
                if sDict[c] > 1:
                    sDict[c] -= 1
                else:
                    sDict.pop(c)
            else:
                return False
        if len(sDict) == 0:
            return True
        return False
