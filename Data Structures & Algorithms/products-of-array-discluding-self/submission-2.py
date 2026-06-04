class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res = [1] * len(nums)
        post = [1] * len(nums)

        mult = 1
        mul = 1
        for i in range(len(nums)):
            res[i] = mult
            post[len(nums)-1-i] = mul
            mul *= nums[len(nums)-1-i]
            mult *= nums[i]
        for i in range(len(nums)):
            res[i] *= post[i]
        return res


        