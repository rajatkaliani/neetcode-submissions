class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        numStack = []
        if len(tokens) == 1:
            return int(tokens[0])
        for t in tokens:
            if t == "+":
                newNum = int(numStack.pop()) + int(numStack.pop())
                numStack.append(newNum)
            elif t == "-":
                b = int(numStack.pop())
                newNum = int(numStack.pop()) - b
                numStack.append(newNum)
            elif t == '*':
                newNum = int(numStack.pop()) * int(numStack.pop())
                numStack.append(newNum)
            elif t == "/":
                b = int(numStack.pop())
                newNum = int(numStack.pop()) / b
                numStack.append(int(newNum))
            else:
                numStack.append(t)
        return numStack[0]
            