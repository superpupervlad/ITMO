import random

fout = open("out.txt", "w")
n = 7500
print(n, file = fout)
for i in range(n):
    print(str(random.randint(-100, 100)) + ' '+ str(random.randint(-100, 100)), file = fout)