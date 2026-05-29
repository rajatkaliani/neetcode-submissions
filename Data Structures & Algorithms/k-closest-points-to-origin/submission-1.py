import heapq
import math
class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for x,y in points:
            euc = math.sqrt((x - 0)**2 + (y - 0)**2)
            heapq.heappush(heap,(-euc,[x,y]))
        while len(heap) > k:
            heapq.heappop(heap)
        res = []
        for dist,point in heap:
            res.append(point)
        return res