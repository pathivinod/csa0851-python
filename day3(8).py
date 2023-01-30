def groupAnagrams(strs):
    anagrams = {}
    for s in strs:
        key = "".join(sorted(s))
        if key in anagrams:
            anagrams[key].append(s)
        else:
            anagrams[key] = [s]
    return list(anagrams.values())
strs = ["eat","tea","tan","ate","nat","bat"]
print(groupAnagrams(strs))
