class Solution:
    import heapq
    from collections import Counter
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        res = []
        for val in count:
            res.append((count[val],val))
        res.sort()
        print(res)
        res = res[::-1]
        res = res[0:k]
        rtrn = []
        for freq,val in res:
            rtrn.append(val)
        return rtrn
