alphabet = int(input())
s = input()
s += '@'
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

answer = [[0 for j in range(alphabet)] for i in range(n)]
for i in range(n):
    for c in range(alphabet):
        if i > 0 and c != ord(s[i]) - 97:
            answer[i][c] = answer[pi[i]][c]
        else:
            answer[i][c] = i + (c == ord(s[i]) - 97)

for line in answer:
    for num in line:
        print(num, end = ' ')
    print()