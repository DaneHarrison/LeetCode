class MinStack:

    def __init__(self):
        self.stack = []
        self.minStack = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)

        minVal = val

        if len(self.minStack) != 0:
            minVal = min(val, self.minStack[-1])

        self.minStack.append(minVal)

    def pop(self) -> None:
        self.stack.pop(-1)
        self.minStack.pop(-1)
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.minStack[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()