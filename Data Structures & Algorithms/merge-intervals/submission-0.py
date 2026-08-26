class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return intervals
        intervals.sort()
        results = [intervals[0]]
        for curEle in intervals[1:]:
            if results[len(results) - 1][1] >= curEle[0]:
                results[len(results) - 1] = [min(results[len(results) - 1][0], curEle[0]),max(results[len(results) - 1][1], curEle[1])]
            else:
                results.append(curEle)
        return results
        