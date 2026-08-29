class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) <= 1:
            return len(nums)
        revList = sorted(nums)
        maxSeq = 1
        curSeq = 1
        prevNum = revList[0]
        print(revList)
        for curNum in revList[1:]:
            print(curNum - prevNum)
            if curNum - prevNum == 1:
                curSeq += 1   
            elif curNum - prevNum > 1:
                if curSeq > maxSeq:
                    maxSeq = curSeq
                curSeq = 1
            print(f"Cur Seq: {curSeq}")
            prevNum = curNum
        return max(maxSeq, curSeq)
        