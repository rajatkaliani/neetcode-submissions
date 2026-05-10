class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l = 0
        r = len(nums) - 1
        while l < r:
            mid = (l+r) // 2
            if nums[mid] < nums[r]:
                r = mid
            else:
                l = mid + 1
        pivot = l

        nl = 0
        rl = len(nums) - 1
        if nums[pivot] <= target <= nums[-1]:
            nl = pivot
        else:
            rl = pivot
        print(nl,rl)
        while nl <= rl:
            mid = (nl+rl) // 2
            if nums[mid] < target:
                nl = mid + 1
            elif nums[mid] > target:
                rl = mid - 1
            else:
                return mid
        return -1


        





       
        
    