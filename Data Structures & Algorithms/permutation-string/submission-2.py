class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1len = len(s1)
        l = 0
        r = s1len 
        while r <= len(s2):
            if (sorted(s2[l:r]) == sorted(s1)):
                return True
            print(s2[l:r])
            l = l + 1
            r = r + 1
        return False