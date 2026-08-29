class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def binarySearchRow(curArray : List[int]) -> bool:
            left = 0
            right = len(curArray) - 1
            while left <= right:
                curMiddle = (left + right) // 2
                if curArray[curMiddle] == target:
                    return True
                elif curArray[curMiddle] < target:
                    left = curMiddle + 1
                elif curArray[curMiddle] > target:
                    right = curMiddle - 1
            return False
        
        for i in range(0, len(matrix)):
            if binarySearchRow(matrix[i]) == True:
                return True
        return False