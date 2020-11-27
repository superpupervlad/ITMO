fin = open("prefix.in")
fout = open("prefix.out", "w")

s = fin.readline()[:-1]
n = len(s)

pi = [0] * (n + 1)
i = 1
j = 0
while i < n:
    if s[i] == s[j]:
        i += 1
        j += 1
        pi[i] = j
    else:
        if j > 0:
            j = pi[j]
        else:
            i += 1
            pi[i] = 0

a = ' '.join(str(pi[i]) for i in range(1, n + 1))
print(a, file = fout, end = '')
fout.close()