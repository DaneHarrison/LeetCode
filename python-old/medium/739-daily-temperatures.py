def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
    tempStack = []
    idxStack = []
    results = [0] * len(temperatures)

    for idx, temp in enumerate(temperatures):
        while len(tempStack) > 0 and tempStack[-1] < temp:
            currIdxFromStack = idxStack.pop()
            tempStack.pop()

            results[currIdxFromStack] = idx - currIdxFromStack

        tempStack.append(temp)
        idxStack.append(idx)
    
    return results