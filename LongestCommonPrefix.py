
def longestCommonPrefix(strs):
    if not strs:
        return ""
    shortest = min(strs, key=len)
    for i, char in enumerate(shortest):
        for string in strs:
            if string[i] != char:
                return shortest[:i]
    return shortest
print(longestCommonPrefix(["flower","flow","flight"]))
