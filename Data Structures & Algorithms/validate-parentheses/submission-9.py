class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        comparisons = {'}':'{',']':'[',')':'('}
        for ch in s:
            if ch in comparisons:
                if len(stack) == 0:
                    return False
                comp = stack.pop()
                if comparisons[ch] != comp:
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

