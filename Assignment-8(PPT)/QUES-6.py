from collections import defaultdict

def findAnagrams(s, p):
    pFreq = defaultdict(int)
    windowFreq = defaultdict(int)

    for char in p:
        pFreq[char] += 1

    left = right = 0
    matchCount = 0
    result = []

    while right < len(s):
        if s[right] in pFreq:
            windowFreq[s[right]] += 1
            if windowFreq[s[right]] <= pFreq[s[right]]:
                matchCount += 1

        if right - left + 1 == len(p):
            if matchCount == len(pFreq):
                result.append(left)

            if s[left] in pFreq:
                windowFreq[s[left]] -= 1
                if windowFreq[s[left]] < pFreq[s[left]]:
                    matchCount -= 1

            left += 1

        right += 1

    return result

# Test the code
s = "cbaebabacd"
p = "abc"
indices = findAnagrams(s, p)
print(indices)
