class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for br in s:
            if (br == '[' or br == '{' or br == '('):
                stack.append(br)
            else:
                if (len(stack) == 0):
                    return False
                out = stack.pop()
                if br == ']':
                    if (out != '[' ):
                        return False
                elif br == ')':
                    if (out != '(' ):
                        return False
                elif br == '}':
                    if (out != '{'):
                        return False
        if (len(stack) == 0):
            return True
        return False

