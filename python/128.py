from typing import List

def longestConsecutive(self, nums: List[int]) -> int:
    numSet = set(nums)
    longest = 0
    
    for num in nums:
        if num - 1 in numSet:
            continue
        
        newLongest = 1
        while num + longest in numSet:
            newLongest += 1
        
        longest = max(longest, newLongest)
    
    return longest