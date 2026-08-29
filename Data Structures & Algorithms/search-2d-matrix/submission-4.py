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
        if len(matrix) == 0:
            return False
        elif len(matrix) == 1:
            return binarySearchRow(matrix[0])
        else:
            i = 0
            while i < len(matrix) - 1:
                if binarySearchRow(matrix[i] + matrix[i+1]):
                    return True
                i += 2
            if len(matrix) % 2 != 0:
                return binarySearchRow(matrix[i])
            return False