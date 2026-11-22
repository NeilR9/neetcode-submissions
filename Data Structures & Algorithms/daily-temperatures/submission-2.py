class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        if len(temperatures) == 1:
            return [0]
        eleStack = []
        indexTrack = []
        result = [0] * len(temperatures)
        i = 0
        while i < len(temperatures):
            if len(eleStack) == 0 or eleStack[-1] >= temperatures[i] :
                eleStack.append(temperatures[i])
                indexTrack.append(i)
                i += 1
            elif eleStack[-1] < temperatures[i]:
                complement = i - indexTrack[-1]
                result[indexTrack[-1]] = complement
                eleStack.pop()
                indexTrack.pop()
        return result
        