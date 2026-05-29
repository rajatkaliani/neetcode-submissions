import heapq
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.kval = k
        heapq.heapify(self.heap)


    def add(self, val: int) -> int:
        heapq.heappush(self.heap,val)
        while len(self.heap) > self.kval:
            heapq.heappop(self.heap)
        return self.heap[0]
        
        
