class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)

        mult = 1
        for i in range(len(nums)):
            res[i] = mult
            mult *= nums[i]
        mult = 1
        for i in range(len(nums)):
            res[len(nums)-i-1] *= mult
            mult *= nums[len(nums) -i - 1]
        return res


        