def calculateZ(s, length):
    Z = [0] * length
    Z[0] = length
    rt = 0
    lt = 0
    for k in range(1, length):
        if k > rt:
            n = 0
            while n + k < length and s[n] == s[n+k]:
                n += 1
            Z[k] = n
            if n > 0:
                lt = k
                rt = k+n-1
        else:
            p = k - lt
            right_part_len = rt - k + 1
            if Z[p] < right_part_len:
                Z[k] = Z[p]
            else:
                i = rt + 1
                while i < length and s[i] == s[i - k]:
                    i += 1
                Z[k] = i - k
                lt = k
                rt = i - 1
    return Z

def search(pattern, text):
    result = []
    N, M = len(text), len(pattern)
    s = '{0}${1}'.format(pattern, text)
    zs = calculateZ(s, len(s))
    for i, z in enumerate(zs):
        if z == M:
            result.append(i - M - 1)
    return result

text = "ABABDABACDABABCABAB"
pattern = "ABABCABAB"
print search(pattern, text)
