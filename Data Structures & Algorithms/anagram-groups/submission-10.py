class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSet = {}
        for n in strs:
            index = "".join(sorted(n))
            if index in strSet:
                strSet[index].append(n)
            else:
                strSet[index] = [n]
        return list(strSet.values())
            