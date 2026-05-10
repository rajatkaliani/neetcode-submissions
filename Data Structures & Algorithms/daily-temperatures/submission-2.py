class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        days = [0]*n
        l = 0
        r = 1
        while l < n - 1:
            print(l,r)
            if r >= len(temperatures):
                l = l + 1
                r = l
            elif temperatures[r] <= temperatures[l]:
                r = r + 1
            else:
                days[l] = r-l
                l = l + 1
                r = l + 1
        return days

