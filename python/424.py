from collections import defaultdict


def characterReplacement(self, s: str, k: int) -> int:
    counts = defaultdict(int)
    maxFreq = 0
    l = 0
    res = 0
    
    for r, rChar in enumerate(s):
        counts[rChar] +=1 
        maxFreq = max(maxFreq, counts[rChar])
        
        while r - l + 1 - maxFreq > k:
            counts[s[l]] -= 1
            l += 1
        
        res = max(res, r - l + 1)
        
    return res