class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numTable = {}
        result = []
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in numTable:
                result = [numTable[diff], i]
                break
            numTable[nums[i]] = i
        return result