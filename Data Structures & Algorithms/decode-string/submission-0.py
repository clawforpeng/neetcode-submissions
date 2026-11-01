class Solution:
    def decodeString(self, s: str) -> str:
        stack = deque()
        i = 0
        digit = ""

        while i < len(s):
            if s[i].isdigit():
                digit += s[i]
            elif s[i] == "[":
                stack.append(int(digit))
                digit = ""
                stack.append("[")
            elif s[i] == "]":
                chars = ""
                while stack[-1] != "[":
                    chars = stack.pop() + chars
                stack.pop() # pop [
                num = stack.pop()
                stack.append(chars * num)
            else:
                stack.append(s[i])
            
            i += 1
        
        return "".join(list(stack))
