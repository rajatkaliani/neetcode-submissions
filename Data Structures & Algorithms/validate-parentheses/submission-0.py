class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        closedKey = {")" : "(", "}" : "{", "]" : "["}
        for b in s:
            if b in closedKey:
                if stack and stack[-1] == closedKey[b]:
                    stack.pop()
                else:
                    return False
            else:
                stack.append(b)
        if not stack:
            return True
        return False 