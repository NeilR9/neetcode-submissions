class MinStack:

    def __init__(self):
        self.minStack = []
        self.minTracker = {}
        self.curIndex = 0
    def push(self, val: int) -> None:
        self.minStack.append(val)
        if len(self.minStack) == 1:
            self.minTracker[self.curIndex] = val
        elif val < self.minTracker[self.curIndex - 1]:
            self.minTracker[self.curIndex] = val
        else:
            self.minTracker[self.curIndex] = self.minTracker[self.curIndex - 1]
        self.curIndex += 1
    def pop(self) -> None:
        top_ele = self.minStack.pop()
        self.minTracker.pop(self.curIndex - 1, "None")
        self.curIndex -= 1
    def top(self) -> int:
        return self.minStack[len(self.minStack) - 1]

    def getMin(self) -> int:
        return self.minTracker[self.curIndex - 1]
