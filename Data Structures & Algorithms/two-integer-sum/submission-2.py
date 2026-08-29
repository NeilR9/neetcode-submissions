class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexLookup = {}
        for i in range(len(nums)):
            if indexLookup.get((target - nums[i]), "None") != "None":
                return [indexLookup[target - nums[i]], i]
            indexLookup[nums[i]] = i