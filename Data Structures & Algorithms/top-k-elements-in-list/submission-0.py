import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numEle = 0
        countMap = dict()
        for i in range(len(nums)):
            if countMap.get(nums[i], "Not Found") == "Not Found":
                countMap[nums[i]] = 1
                numEle += 1
                continue
            countMap[nums[i]] += 1
        heapList = list(zip(list(countMap.values()), list(countMap)))
        heapq.heapify(heapList)
        i = 0
        while i < numEle - k:
            heapq.heappop(heapList)
            i += 1
        result = []
        i = k
        while i > 0:
            result.append(heapList[0][1])
            heapq.heappop(heapList)
            i -= 1
        return result


        
        
