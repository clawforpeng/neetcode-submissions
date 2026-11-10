class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack = deque()

        for op in operations:
            if op == "+":
                if len(stack) > 1:
                    stack.append(stack[-1] + stack[-2])
            elif op == "D":
                if len(stack) > 0:
                    stack.append(stack[-1] * 2)
            elif op == "C":
                if len(stack) > 0:
                    stack.pop()
            else:
                stack.append(int(op))
        
        score = 0
        for val in stack:
            score += val

        return score