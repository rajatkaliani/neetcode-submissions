class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = 0
        t_count = 0
        for c in s:
            s_count += ord(c)
        for c in t:
            t_count += ord(c)
        return chr(t_count-s_count)