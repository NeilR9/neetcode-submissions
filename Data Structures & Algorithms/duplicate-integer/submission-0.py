class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        curDict = {}
        for curNum in nums:
            if curDict.get(curNum, "Null") == "Null":
                curDict[curNum] = 1
            else:
                return True
        return False
        