class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = defaultdict(list)

        for num in nums:
            if num in count.keys():
                count[num] = count[num] + 1
            else:
                count[num] = 1
        sorted_items = dict(sorted(count.items(), key=lambda x: x[1], reverse=True))
        return list(sorted_items.keys())[:k]