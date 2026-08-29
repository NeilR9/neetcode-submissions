class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sumList = []
        def checkList(firstNum: int, secondNum: int, thirdNum: int):
            for i in range(0, len(sumList)):
                if firstNum in sumList[i] and secondNum in sumList[i] and thirdNum in sumList[i]:
                    return False
            return True
        if len(nums) < 3:
            return []
        firstPointer = 0
        secondPointer = firstPointer + 1
        thirdPointer = secondPointer + 1
        while firstPointer < len(nums) - 2:
            #print(f"First Pointer: {firstPointer}")
            #print(f"Second Pointer: {secondPointer}")
            #print(f"Third Pointer: {thirdPointer}")
            if nums[firstPointer] + nums[secondPointer] + nums[thirdPointer] == 0:
                if checkList(nums[firstPointer], nums[secondPointer], nums[thirdPointer]):
                    sumList.append([nums[firstPointer], nums[secondPointer], nums[thirdPointer]])
            if thirdPointer == len(nums) - 1 and secondPointer == len(nums) - 2:
                firstPointer += 1
                secondPointer = firstPointer + 1
                thirdPointer = secondPointer + 1
            elif thirdPointer == len(nums) - 1 and secondPointer < len(nums) - 2:
                secondPointer += 1
                thirdPointer = secondPointer + 1
            else:
                thirdPointer += 1
        return sumList