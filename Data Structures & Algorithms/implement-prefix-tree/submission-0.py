class PrefixTree:

    def __init__(self):
        self.stack = []

    def insert(self, word: str) -> None:
        self.stack.append(word)

    def search(self, word: str) -> bool:
        for i in range(0, len(self.stack)):
            if self.stack[i] == word:
                return True
        return False

    def startsWith(self, prefix: str) -> bool:
        print(f"Prefix: {prefix}")
        for i in range(0, len(self.stack)):
            if (self.stack[i])[0:len(prefix)] == prefix:
                return True
        return False
        