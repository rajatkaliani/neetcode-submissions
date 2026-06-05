class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        red = 0
        white = 0
        blue = len(nums) - 1
        i = 0
        while i <= blue:
            if nums[i] == 0:
                temp = nums[red]
                nums[red] = nums[i]
                nums[i] = temp
                i = i + 1
                red = red + 1
            elif nums[i] == 2:
                temp = nums[blue]
                nums[blue] = nums[i]
                nums[i] = temp
                blue = blue - 1
            else:
                i = i + 1
        return nums


        