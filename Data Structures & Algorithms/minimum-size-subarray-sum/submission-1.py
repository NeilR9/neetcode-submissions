class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if len(nums) == 1:
            if (nums[0] == target):
                return 1
            return 0
        minLength = 0
        found = False
        for i in range(len(nums)):
            count = 1
            curSum = nums[i]
            j = i+1
            while curSum < target and j < len(nums):
                count += 1
                curSum += nums[j]
                j += 1
            if curSum >= target:
                if found == False:
                    found = True
                    minLength = count
                    continue
                minLength = min(minLength, count)
        return minLength
        