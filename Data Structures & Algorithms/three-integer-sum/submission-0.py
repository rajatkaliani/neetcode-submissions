class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        rtrn = set()
        for i in range(len(nums)):
            for j in range(len(nums)):
                for k in range(len(nums)):
                    if nums[i]+nums[j]+nums[k] == 0 and i!=j and i!=k and j!=k:
                        rtrn.add(tuple(sorted([nums[i],nums[j],nums[k]])))
        return list(rtrn)
    