class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sets = defaultdict(list)
        for word in strs:
            defi = "".join(sorted(word))
            print(defi)
            sets[defi].append(word)
        return list(sets.values())


        