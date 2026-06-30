class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        zipped = zip(names,heights)

        sort = sorted(zipped, key=lambda x: x[1], reverse=True)

        res = []
        for name,height in sort:
            res.append(name)
        return res