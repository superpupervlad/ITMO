from PIL import ImageDraw, Image
import math

image = Image.open('test.bmp')  # Открываем изображение
draw = ImageDraw.Draw(image)  # Объявляем переменную для создания нового изображения
width = image.size[0]  # Ширина
height = image.size[1]  # Высота
pix = image.load()  # Значения пикселей

# Округляем среднюю строку
unique = set()  # Задаем множество уникальных значений
count = [0]*14  # Счетчик округленных значений
middle_w = width//2
for x in range(width):
    grey = pix[x, middle_w][0]
    grey = round(grey / 20)
    count[grey] += 1
    grey *= 20
    unique.add(grey)
    draw.point((x, middle_w), (grey, grey, grey))  # Изменяем пиксель для финального изображения
    print(pix[x, middle_w][0], end=' ')
# Вычисляем энтропию
print("\n")
entropy = 0
for i in range(0, 14):
    if count[i] != 0:
        p = count[i] / 128
        entropy += p * math.log(p, 2)
entropy *= -1
for x in range(width):
    grey = pix[x, middle_w][0]
    grey = round(grey / 20) *20
    if grey == 20:
        print('1010',end = '   ')
    elif grey == 60:
        print('11010',end = '   ')
    elif grey == 80:
        print('11011',end = '   ')
    elif grey == 100:
        print('1011',end = '   ')
    elif grey == 120:
        print('1100',end = '   ')
    elif grey == 140:
        print('1110',end = '   ')
    elif grey == 160:
        print('100',end = '   ')
    elif grey == 180:
        print('01',end = '   ')
    elif grey == 200:
        print('00',end = '   ')
    elif grey == 220:
        print('1111',end = '   ')
print('\n')
print(count)
print('Количество символов алфавита: ' + str(unique))
print('Энтропия: ' + str(entropy))
print('Средняя длина двоичного кода: ???')
image.save("result.bmp", "bmp")  # Сохраняем изображение
for i in range(width):
    print(pix[x, middle_w][0],end = ' ')
