class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for elm in nums:
            if elm in seen:
                return True
            seen.add(elm)
        return False
        