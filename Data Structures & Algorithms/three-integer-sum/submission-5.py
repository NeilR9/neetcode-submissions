class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        sumList = []
        def checkList(firstNum: int, secondNum: int, thirdNum: int):
            """
            if nums[firstPointer] == 0 and nums[secondPointer] == 0 and nums[thirdPointer] == 0:
                    print("Checking the 0!")
            """
            givenArray = sorted([firstNum, secondNum, thirdNum])
            for i in range(0, len(sumList)):
                if givenArray[0] == sumList[i][0] and givenArray[1] == sumList[i][1] and givenArray[2] == sumList[i][2]:
                    """
                    if nums[firstPointer] == 0 and nums[secondPointer] == 0 and nums[thirdPointer] == 0:
                        print(f"The List: [{sumList[i][0]}, {sumList[i][1]}, {sumList[i][2]}]")
                    """
                    return False
            #print(f"First Num: {firstNum}, Second Num: {secondNum}, Third Num: {thirdNum}")
            return True
        if len(nums) < 3:
            return []
        firstPointer = 0
        secondPointer = firstPointer + 1
        thirdPointer = secondPointer + 1
        while firstPointer < len(nums) - 2:
            """
            if nums[firstPointer] == 0 and nums[secondPointer] == 0 and nums[thirdPointer] == 0:
                print("They are all 0s")
            """
            #print(f"First Pointer: {firstPointer}")
            #print(f"Second Pointer: {secondPointer}")
            #print(f"Third Pointer: {thirdPointer}")
            if nums[firstPointer] + nums[secondPointer] + nums[thirdPointer] == 0:
                """
                if nums[firstPointer] == 0 and nums[secondPointer] == 0 and nums[thirdPointer] == 0:
                    print("Sum is 0!")
                """
                if checkList(nums[firstPointer], nums[secondPointer], nums[thirdPointer]):
                    sumList.append(sorted([nums[firstPointer], nums[secondPointer], nums[thirdPointer]]))
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