def lengthOfLongestSubstring(self, s: str) -> int:
    charSet = set()
    maxLength = 0
    l = 0
    
    for r, char in enumerate(s):
        while char in charSet:
            charSet.remove(s[l])
            l += 1
            
        maxLength = max(maxLength, r - l + 1)
        charSet.add(char)
    
    return maxLength
    
    