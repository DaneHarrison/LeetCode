from typing import List

def run(nums: List[int], target: int) -> List[int]:
    diffs = {}
    
    for idx, num in enumerate(nums):
        newDiff = target - num
        exsitingIdx = diffs.get(newDiff, None)
        
        if exsitingIdx != None:
            return [exsitingIdx, idx]
        
        diffs[newDiff] = idx