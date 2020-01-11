from PIL import Image, ImageDraw
import math

image = Image.open("2.png")
draw = ImageDraw.Draw(image)
width = image.size[0]
height = image.size[1]
pix = image.load()



value = []
Freq = [0] * 14
array = set()


for x in range(width):
    r = pix[x, height // 2][0]
    g = pix[x, height // 2][1]
    b = pix[x, height // 2][2]
    sr = ((r + g + b) // 3)
    array.add(sr)
    value.append(sr)
    sr = round(sr / 20)
    Freq[sr] += 1
    sr *= 20
    
k = len(array)
sumi = 0

for i in range(1, k + 1):
    s = 1 / i 
    sumi += (s) * math.log(s, 2)
    
sumi *= -1

for x in range(width):
    print(pix[x, height // 2][0])
print(len(array))
print(sumi) 
print(Freq)
