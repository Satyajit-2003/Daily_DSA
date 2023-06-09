class MinStack:

    def __init__(self):
        self.stack = []
        self.mini = [float('inf')]

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.mini.append(min(self.mini[-1],val))

    def pop(self) -> None:
        self.stack.pop()
        self.mini.pop()        

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.mini[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

if __name__ == '__main__':
    s = MinStack()
    s.push(-2)
    s.push(0)
    s.push(-3)
    print(s.getMin())
    s.pop()
    print(s.top())
    print(s.getMin())
    s.push(-5)
    print(s.getMin())
