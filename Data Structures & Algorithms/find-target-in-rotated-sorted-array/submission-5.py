class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if (nums[mid] > nums[r]):
                l = mid + 1
            else:
                r = mid
        pivot = l
        if nums[l] == target:
            return l
        if nums[l] <= target <= nums[-1]:
            l = pivot
            r = len(nums) - 1
        else:
            l = 0
            r = pivot
        
        while l < r:
            mid = (l+r) // 2
            if (target > nums[mid]):
                l = mid + 1
            else:
                r = mid
        if nums[l] == target:
            return l
        return -1

        
        





       
        
    