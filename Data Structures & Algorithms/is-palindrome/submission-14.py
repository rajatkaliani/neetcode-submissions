class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ", "")
        l,r = 0, len(s)-1
        while (l < r):
            while(not s[r].isalnum() and l < r):
                r = r-1
            while(not s[l].isalnum() and l < r):
                l = l + 1
            if (s[l].lower() != s[r].lower()):
                return False
            r = r -1
            l = l + 1
        return True