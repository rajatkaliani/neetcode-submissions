class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        def backtrack(index, path):
            sumi = sum(path)
            if sumi == target and path not in res:
                res.append(path[:])
                return
            elif sumi > target or len(nums) == index:
                return
            path.append(nums[index])
            backtrack(index,path)

            backtrack(index+1,path)

            path.pop()
            backtrack(index+1,path)


            
        
        backtrack(0,[])
        return res
