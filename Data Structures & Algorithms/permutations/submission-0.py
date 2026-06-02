class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res = []

        def backtrack(curr,perm):
            if len(curr) == 0:
                res.append(perm[:])
                return
            for i in range(len(curr)):
                perm.append(curr[i])
                elm = curr.pop(i)
                backtrack(curr,perm)
                perm.pop()
                curr.insert(i,elm)
        backtrack(nums,[])
        return res