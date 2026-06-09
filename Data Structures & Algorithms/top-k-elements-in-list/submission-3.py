class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = Counter(nums)
        heap = []
        for val in counts:
            heapq.heappush(heap,(counts[val],val))
            if len(heap) > k:
                heapq.heappop(heap)
        res = []
        for elm in heap:
            res.append(elm[1])
        return res