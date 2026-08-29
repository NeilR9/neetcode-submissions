from collections import defaultdict
class LRUCache:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.curDict = defaultdict()
        self.keySet = []

    def get(self, key: int) -> int:
        print("Get method:")
        if self.curDict.get(key, 'Not Found') == 'Not Found':
            return -1
        result = self.curDict[key]
        self.curDict.pop(key)
        self.keySet.remove(key)
        self.curDict[key] = result
        self.keySet.append(key)
        print(self.curDict)
        return result

    def put(self, key: int, value: int) -> None:
        
        if self.capacity == 0 and self.curDict.get(key, 'Not Found') == 'Not Found':
            self.curDict.pop(self.keySet[0])
            self.keySet.pop(0)
        elif key in self.curDict:
            self.curDict.pop(key)
            self.keySet.remove(key)
        else:
            self.capacity -= 1
        self.curDict[key] = value
        self.keySet.append(key)
        print(self.curDict)
        print(self.keySet)
