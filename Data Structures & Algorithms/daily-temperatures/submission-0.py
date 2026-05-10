class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = [0]*len(temperatures)
        stack = []
        for index,elm in enumerate(temperatures):
            while stack and elm > stack[-1][0]:
                stackT, stackIndex = stack.pop()
                output[stackIndex] = (index - stackIndex)
            stack.append([elm,index])
        return output

