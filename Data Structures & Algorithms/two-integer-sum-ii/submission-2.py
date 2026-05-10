class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i,num in enumerate(numbers):
            for j,n in enumerate(numbers):
                if num+n == target:
                    return [i+1,j+1]