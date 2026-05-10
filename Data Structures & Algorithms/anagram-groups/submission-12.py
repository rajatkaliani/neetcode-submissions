class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        strSet = {}
        for string in strs:
            index = "".join(sorted(string))
            print(index)
            if index in strSet:
                strSet[index].append(string)
            else:
                strSet[index] = [string]
        return list(strSet.values())
            