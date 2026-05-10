class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1
        while l <= r:
            print(str(l) + "left" + "\n")
            print(str(r) + "right" + "\n")
            mid = (l+r)//2
            print(str(mid) + "mid" + "\n")
            if nums[mid] > target:
                r = mid - 1
            elif nums[mid] < target:
                l = mid + 1
            elif nums[mid] == target:
                return mid
        return -1
            
