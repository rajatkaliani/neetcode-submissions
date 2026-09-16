class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj = {}
        for i in range(1,n+1):
            adj[i] = []
        for src,target,dist in times:
            adj[src].append([target,dist])
        shortest = {}
        minHeap = [[0,k]]
        while minHeap:
            weight,node = heapq.heappop(minHeap)
            if node in shortest:
                continue
            shortest[node] = weight
            for target,distance in adj[node]:
                if target not in shortest:
                    heapq.heappush(minHeap,[distance+weight,target])
        print(shortest)
        sumi = 0
        if len(shortest) != n:
            return -1
        return max(shortest.values())