def KMPSearch(pattern, text):
    M = len(pattern)
    N = len(text)
    lps = [0]*M
    computeLPSArray(pattern, M, lps)
    i, j = 0, 0
    while i < N:
        if pattern[j] == text[i]:
            i += 1
            j += 1
        if j == M:
            print "Found patterntern at index " + str(i-j)
            j = lps[j-1]
        elif i < N and pattern[j] != text[i]:
            if j != 0:
                j = lps[j-1]
            else:
                i += 1
 
def computeLPSArray(pattern, M, lps):
    length = 0
    i = 1
    while i < M:
        if pattern[i]==pattern[length]:
            length += 1
            lps[i] = length
            i += 1
        else:
            if length != 0:
                length = lps[length-1]
            else:
                lps[i] = 0
                i += 1
 
text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
KMPSearch(pattern, text)
