class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == '}':
                if len(stack) == 0:
                    return False
                comp = stack.pop()
                if comp != "{":
                    return False
            elif ch == ')':
                if len(stack) == 0:
                    return False
                comp = stack.pop()
                if comp != "(":
                    return False
            elif ch == ']':
                if len(stack) == 0:
                    return False
                comp = stack.pop()
                if comp != "[":
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0

