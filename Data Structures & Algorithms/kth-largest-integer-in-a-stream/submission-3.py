import heapq
class KthLargest:
    min_heap = []
    kthLargest = -1
    def __init__(self, k: int, nums: List[int]):
        self.min_heap = nums
        heapq.heapify(self.min_heap)
        self.kthLargest = k
        #print(f"Initial Heap: {self.min_heap}")
        i = 0
        initialRoot = len(self.min_heap) - self.kthLargest
        while i < initialRoot:
            heapq.heappop(self.min_heap)
            i += 1
            #print(f"Value of i: {i}")
            #print(f"Revised root index: {len(self.min_heap) - self.kthLargest}")
        #print(f"Heap: {self.min_heap}")


    def add(self, val: int) -> int:
        heapq.heappush(self.min_heap, val)
        if len(self.min_heap) > self.kthLargest:
            heapq.heappop(self.min_heap)
        return self.min_heap[0]
