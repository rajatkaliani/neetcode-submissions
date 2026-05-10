class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        output = []
        while (len(temperatures) > 1):
            numDays = 0
            greater = False
            temp = temperatures[0]
            temperatures = temperatures[1:]
            for elm in temperatures:
                if(elm <= temp):
                    numDays = numDays + 1
                elif(elm > temp):
                    greater = True
                    numDays = numDays + 1
                    break
            if (not greater):
                numDays = 0
            output.append(numDays)
            print(str(output))
            numDays = 0
        output.append(0)
        return output