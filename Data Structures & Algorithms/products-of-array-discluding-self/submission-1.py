class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        skip = 0
        new = [1]*len(nums)
        while skip < len(nums):
            rep = 1
            itr = 0
            while itr < len(nums):
                if itr != skip:
                    rep = rep * nums[itr]
                itr = itr + 1
            new[skip] = rep
            skip = skip + 1
        return new



        