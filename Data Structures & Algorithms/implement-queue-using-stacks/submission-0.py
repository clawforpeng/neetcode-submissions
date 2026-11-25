class MyQueue:

    def __init__(self):
        self.pending = deque()
        self.queue = deque()

    def push(self, x: int) -> None:
        self.pending.append(x)

    def pop(self) -> int:
        if self.queue:
            return self.queue.pop()
        
        while self.pending:
            item = self.pending.pop()
            self.queue.append(item)
        
        return self.queue.pop()
        

    def peek(self) -> int:
        if self.queue:
            return self.queue[-1]
        
        while self.pending:
            item = self.pending.pop()
            self.queue.append(item)
        
        return self.queue[-1]

    def empty(self) -> bool:
        if not self.queue and not self.pending:
            return True
        return False


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()