class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        output = 0
        for token in tokens:
            if (token not in '+-*/'):
                token = int(token)
                stack.append(token)
            elif(token == '+'):
                stack.append(stack.pop() + stack.pop())
            elif(token == '-'):
                stack.append(-(stack.pop()) + stack.pop())
            elif(token == '*'):
                stack.append(stack.pop() * stack.pop())
            elif(token == '/'):
                first = stack.pop()
                stack.append(int(stack.pop() / first))
            print(stack)
        return int(stack[0])


