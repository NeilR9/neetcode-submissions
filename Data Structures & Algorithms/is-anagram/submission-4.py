class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if s == t:
            return True
        if len(s) != len(t):
            return False
        sCount = {}
        tCount = {}
        for curChar in s:
            if curChar not in sCount:
                sCount[curChar] = 1
                continue
            sCount[curChar] += 1
        for curChar in t:
            if curChar not in tCount:
                tCount[curChar] = 1
                continue
            tCount[curChar] += 1
        return sCount == tCount
        