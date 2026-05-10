class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maxA = 0
        l = 0
        r = len(heights)-1
        while l < r:
            maxA = max(maxA,(r-l)*min(heights[l],heights[r]))
            if heights[l] < heights[r]:
                l = l + 1
            else:
                r = r - 1
        return maxA