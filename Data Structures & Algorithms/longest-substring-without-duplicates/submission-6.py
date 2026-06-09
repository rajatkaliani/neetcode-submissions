class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s:
            return 0
        l = 0
        r = 0
        seen = set()
        maxi = 0
        while r < len(s):
            while s[r] in seen:
                seen.remove(s[l])
                l = l + 1
            seen.add(s[r])
            maxi = max(maxi,r-l+1)
            r = r + 1
        return maxi
        
            
