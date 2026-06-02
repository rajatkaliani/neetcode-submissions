class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res = []
        def backtrack(curr, index):
            if index == len(nums):
                if curr not in res:
                    res.append(curr[:])
                return

            curr.append(nums[index])
            backtrack(curr,index+1)

            curr.pop()
            backtrack(curr,index+1)
        backtrack([],0)
        return res
            
