class MinStack:

    def __init__(self):
        self.curList = []
        self.minVisited = []
        self.minEle = 0
        self.length = 0
    def push(self, val: int) -> None:
        if self.length == 0:
            self.minEle = val
        elif val < self.minEle:
            self.minEle = val
        self.curList.append(val)
        self.minVisited.append(self.minEle)
        self.length += 1
    def pop(self) -> None:
        self.curList = self.curList[0:self.length - 1]
        self.minVisited = self.minVisited[0:self.length - 1]
        self.length -= 1
        if self.length > 0:
            self.minEle = self.minVisited[self.length - 1]
    def top(self) -> int:
        return self.curList[self.length - 1]

    def getMin(self) -> int:
        return self.minEle        
