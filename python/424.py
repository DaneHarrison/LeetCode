from collections import defaultdict


def characterReplacement(self, s: str, k: int) -> int:
    counts = defaultdict(int)
    maxFreq = 0
    l = 0
    res = 0
    
    for r, rChar in enumerate(s):
        counts[rChar] +=1 
        maxFreq = max(maxFreq, counts[rChar])
        length = r - l + 1
        
        while length - maxFreq > k:
            counts[s[l]] -= 1
            l += 1
        
        length = r - l + 1
        res = max(res, length)
        
    return res