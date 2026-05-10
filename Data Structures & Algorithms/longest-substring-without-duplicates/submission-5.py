class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        seen = set()
        max_len = 0
        while r < len(s):
            if s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            else:
                seen.add(s[r])
                r = r + 1
                max_len = max(max_len, r - l)

        return max_len
        
            
