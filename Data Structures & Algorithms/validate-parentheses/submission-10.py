class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for ch in s:
            if ch == ']':
                if len(stack) == 0 or stack.pop() != '[':
                    return False
            elif ch == ")":
                if len(stack) == 0 or stack.pop() != '(':
                    return False
            elif ch == '}':
                if len(stack) == 0 or stack.pop() != '{':
                    return False
            else:
                stack.append(ch)
        return len(stack) == 0