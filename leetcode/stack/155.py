class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = [-9999999]

    def push(self, val: int) -> None:
        min = self.min_stack[-1]
        
        if val < min:
            self.min_stack.append(val)
        else:
            self.min_stack.append(min)
            
        self.stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]