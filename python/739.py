from typing import List

def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    res = [0 for _ in range(len(temperatures))]
    tempsStack = []
    tempsIdx = []
    
    for idx, temperature in enumerate(temperatures):        
        while len(tempsStack) > 0 and tempsStack[-1] < temperature:
            tempsStack.pop()
            lowerTempIdx = tempsIdx.pop()
            numDays = idx - lowerTempIdx
            res[lowerTempIdx] = numDays
            
        tempsStack.append(temperature)
        tempsIdx.append(idx)

    return res