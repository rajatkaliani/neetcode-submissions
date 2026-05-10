class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_dict = {}
        t_dict = {}
        for e in s:
            if e in s_dict.keys():
                s_dict[e] = s_dict[e] + 1
            else:
                s_dict[e] = 1
        for e in t:
            if e in t_dict.keys():
                t_dict[e] = t_dict[e] + 1
            else:
                t_dict[e] = 1
        print(str(s_dict) + "\n" + str(t_dict))
        return s_dict == t_dict
            