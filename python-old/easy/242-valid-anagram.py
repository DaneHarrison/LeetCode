def isAnagram(self, s, t):
    if len(s) != len(t):
            return False
    
    sDict = {}
    tDict = {}

    for char in s:
        sDict[char] = (sDict.get(char) or 0) + 1

    for char in t:
        tDict[char] = (tDict.get(char) or 0) + 1

    return sDict == tDict