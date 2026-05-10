class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l,r = 0,len(numbers) - 1
        
        while numbers[l] + numbers[r] != target and l!=r:
            summ = numbers[l] + numbers[r]
            if (summ < target):
                l = l + 1
            else:
                r = r-1
        return [l+1,r+1]

        