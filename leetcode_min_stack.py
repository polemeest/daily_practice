class MinStack:

    def __init__(self):
        self.stack = list()
        self.min = [float("inf"),]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min.append(min(val, self.min[-1]))

    def pop(self) -> None:
        last = self.stack.pop(-1)
        self.min.pop(-1) 
        return last

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()