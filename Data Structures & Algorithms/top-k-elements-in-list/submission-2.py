class Solution:
    import heapq
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(int)
        heap = []
        for elm in nums:
            if count[elm] == 0:
                count[elm] = 1
            else:
                count[elm] = count[elm] + 1


        for num,freq in count.items():
            heapq.heappush(heap,(-freq,num))
        rtrn = []
        for i in range(k):
            new = heapq.heappop(heap)[1]
            rtrn.append(new)
        return rtrn