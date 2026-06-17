class Solution:
    def encode(self, strs: List[str]) -> str:
        encoded_str = ""
        for string in strs:
            encoded_str += str(len(string)) + "#" + string
        return encoded_str

    def decode(self, s: str) -> List[str]:
        i = 0
        sols = []
        length = ""
        while i < len(s):
            if s[i] != "#":
                length += s[i]
                i += 1
            else:
                length = int(length)
                string = s[i + 1 : i + 1 + length]
                sols.append(string)
                i = i + 1 + length
                length = ""
        return sols