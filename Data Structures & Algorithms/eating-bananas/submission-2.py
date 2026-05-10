class Solution:
    import math
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        rn = range(1,max(piles)+1)
        l = 0
        r = len(rn) - 1
        print("l " + str(rn[l]) + " r " + str(rn[r]))

        while l < r:
            mid = (l+r) // 2
            count = 0
            print("Diver" + str(rn[mid]))
            for p in piles:
                count += math.ceil((p / rn[mid]))
            print(str(count) + " Counted") 
            if count <= h:
                r = mid
            else:
                l = mid + 1
            print("l " + str(rn[l]) + " r " + str(rn[r]))
        return rn[l]
            





