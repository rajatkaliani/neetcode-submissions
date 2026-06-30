from collections import defaultdict
class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        ctr = defaultdict(int)
        for w in words:
            for c in w:
                ctr[c] += 1
        print(ctr.keys(),ctr.values())
        for num in ctr.values():
            if num % len(words) != 0:
                return False
        return True
