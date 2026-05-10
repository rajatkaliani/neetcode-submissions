class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numIndex = {}
        for i,n in enumerate(nums):
            if (target-n) in numIndex:
                return [numIndex[target-n],i]
            comp = target - n
            numIndex[n] = i
