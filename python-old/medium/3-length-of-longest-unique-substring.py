def lengthOfLongestSubstring(self, s: str) -> int:
    best = 0
    substring = ""

    for char in s:
        if char in substring:
            best = max(best, len(substring))
            posiOfPrev = substring.find(char)
            substring = substring[posiOfPrev + 1:]
        
        substring += char

    best = max(best, len(substring))

    return best