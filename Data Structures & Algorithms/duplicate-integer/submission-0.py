class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        non = set(nums)
        return len(non) != len(nums)