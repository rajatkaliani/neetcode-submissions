class Solution:
    from collections import Counter
    def findTheDifference(self, s: str, t: str) -> str:
        s_count = Counter(s)
        t_count = Counter(t)
        for key in t_count.keys():
            if s_count[key] != t_count[key]:
                return key