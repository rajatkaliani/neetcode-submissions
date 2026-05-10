class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        s = []
        res = 0
        for t in tokens:
            print(s)
            if t.lstrip("-").isdigit():
                s.append(int(t))
            else:
                b = s.pop()
                a = s.pop()
                if t == "+":
                    s.append(a+b)
                elif t == "-":
                    s.append(a-b)
                elif t == "/":
                    s.append(int(a/b))
                elif t == "*":
                    s.append(a*b)
        return s[-1]

