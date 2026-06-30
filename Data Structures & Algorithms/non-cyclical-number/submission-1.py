class Solution:
    def isHappy(self, n: int) -> bool:
        val = 0
        seen = set()
        while val != 1:
            val = 0
            for elm in str(n):
                val += (int(elm)*int(elm))
            if val in seen:
                return False
            seen.add(val)
            n = val
        return True