class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)
        s = count.most_common(k)
        rtn = []
        for tup in s:
            rtn.append(tup[0])
        return rtn
