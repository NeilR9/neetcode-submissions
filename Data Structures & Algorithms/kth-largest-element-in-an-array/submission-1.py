import heapq
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)
        curIndex = 0
        target = 0
        targetIndex = len(nums) - k + 1
        while curIndex < targetIndex:
            target = heapq.heappop(nums)
            curIndex += 1
        return target
        