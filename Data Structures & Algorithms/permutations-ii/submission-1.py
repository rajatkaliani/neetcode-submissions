class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        res = set()
        used = []
        def backtrack(per):
            if len(per) == len(nums):
                res.add(tuple(per[:]))
                return
            for i in range(len(nums)):
                if i not in used and nums[i] not in res:
                    per.append(nums[i])
                    used.append(i)
                    backtrack(per)
                    used.pop()
                    per.pop()
        backtrack([])
        return list(res)
