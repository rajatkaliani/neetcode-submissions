class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxi = 0
        l = 0
        r = len(heights) - 1
        while l < r:
            maxi = max((r-l)*min(heights[l],heights[r]),maxi)
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r -1
        return maxi