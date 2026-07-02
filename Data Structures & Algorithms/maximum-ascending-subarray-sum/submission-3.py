class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        maxi = sumi = nums[0]
        l = 1
        while l < len(nums):
            if nums[l-1] < nums[l]:
                sumi += nums[l]
            else:
                sumi = nums[l]
            l = l + 1
            maxi = max(maxi,sumi)
        return maxi