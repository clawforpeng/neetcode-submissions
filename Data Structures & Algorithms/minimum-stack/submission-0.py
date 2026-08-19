class MinStack:

    def __init__(self):
        self.stack = deque()
        self.minStack = deque()

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.minStack:
            self.minStack.append(min(val, self.minStack[-1]))
        else:
            self.minStack.append(val)

    def pop(self) -> None:
        if self.stack:
            self.stack.pop()
        if self.minStack:
            self.minStack.pop()

    def top(self) -> int:
        if self.stack:
            return self.stack[-1]
        return -1
        
    def getMin(self) -> int:
        if self.minStack:
            return self.minStack[-1]
        return -1
