class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l = 0
        maxi = 0
        r = len(heights)-1
        while l < r:
            mini = min(heights[l],heights[r])
            maxi = max((mini * (r-l)),maxi)
            print(str(l) + "   " + str(r))
            if (heights[l] <= heights[r]):
                
                l = l + 1
            else:
                r = r - 1
        
        return maxi