def groupAnagrams(self, strs):
    sigs = {}

    for curr in strs:
        sigKey = "".join(sorted(curr))
        listed = sigs.get(sigKey, [])
        listed.append(curr)
        sigs[sigKey] = listed
        
    return sigs.values()