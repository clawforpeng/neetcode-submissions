class Solution:
    def checkValidString(self, s: str) -> bool:
        stack = deque()
        wildCards = deque()

        for i, c in enumerate(s):
            if c == "(":
                stack.append(i)
            elif c == ")":
                if len(stack):
                    stack.pop()
                elif len(wildCards):
                    wildCards.pop()
                else:
                    return False
            else:
                wildCards.append(i)
        

        while stack:
            i = stack.pop()

            if wildCards and wildCards.pop() > i:
                continue
            return False


        return True

# ***(