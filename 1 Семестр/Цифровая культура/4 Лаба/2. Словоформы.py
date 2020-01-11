def count_words(text):  # 2.1
    count = 0
    for line in text:
        count += len(line)
    return count


def unique_count(text):  # 2.2
    unique = set()
    for line in text:
        for word in line:
            unique.add(word)
    return unique


def words_in_dic(words):  # 2.3
    count = 0
    for word in words:
        if word in new_dic1:
            count += 1
    return count


def word_forms(dictionary):  # 2.4
    check = 0
    slovoforms = dict()
    count = 0
    c = 0
    a = 0
    for elem in words:
        for line in dictionary:
            check = 0
            line = line.split(',')
            for word in line:
                if elem == word:
                    count += 1
                    if line[0] in slovoforms:
                        slovoforms[line[0]][0] += 1
                        slovoforms[line[0]][1].append(elem)
                    else:
                        slovoforms[line[0]] = [1, [word]]
                    check = 1
                    break
                c += 1
            if check == 1:
                break
        if check == 0:
            if elem in slovoforms:
                slovoforms[line[0]][0] += 1
                slovoforms[line[0]][1].append(elem)
            else:
                slovoforms[line[0]] = [1, [word]]
        a += 1
        print(str(a / 760 * 100) + "%")
    print("Статистика по словоформам: " + str(slovoforms))
    print("Уникальных слообразований: " + str(len(slovoforms)))
    print("Всего операций: " + str(c))
    return slovoforms


def words_not_in_dic(words):
    w = []
    for word in words:
        if word not in new_dic1:
            w.append(word)
    return w


def lev_dist(a,b):
    n, m = len(a), len(b)
    if n > m:
        a, b = b, a
        n, m = m, n

    current_row = range(n + 1)
    for i in range(1, m + 1):
        previous_row, current_row = current_row, [i] + [0] * n
        for j in range(1, n + 1):
            add, delete, change = previous_row[j] + 1, current_row[j - 1] + 1, previous_row[j - 1]
            if a[j - 1] != b[i - 1]:
                change += 1
            current_row[j] = min(add, delete, change)
    return current_row[n]


def find_bad_words():
    array = []
    for word1 in not_in_dic:
        minimum = 999
        temp = []
        for word2 in new_dic1:
            distance = lev_dist(word1, word2)
            if distance <= minimum:
                minimum = distance
                temp.append([minimum, word2])
        minimum = min(temp)[0]
        i = 0
        for j in range(len(temp)):
            if temp[i][0] > minimum:
                temp.pop(i)
                i -= 1
            i += 1
        for a in temp:
            for b in new_dic1:
                if a[1] == b:
                    a[0] = new_dic1[b]
        real_minimum = temp.index(min(temp))
        array.append([word1, temp[real_minimum][1], minimum])
        if minimum > 2:
            print('Возможная ошибка "' + str(word1) + '" | Мин. редакторское расстояние: ' + str(minimum) +
                  ' | Возможные замены: ' + str([temp[i][1] for i in range(len(temp))])
                  + ' | Замены нет из-за большого ред. расстояния')
        else:
            print('Возможная ошибка "' + str(word1) + '" | Мин. редакторское расстояние: ' + str(minimum) +
                  ' | Возможные замены: ' + str([temp[i][1] for i in range(len(temp))]) + ' | Вероятная замена: ' +
                  str(temp[real_minimum][1]))
    return array


print('----------------------------Подготовка и Задание 1----------------------------')
fin = open("brain216.txt", encoding="utf8")
fout = open("text_without_signs.txt", "w")
lines_in_original_file = 0

for line in fin:
    line = line.replace("!", "").replace("?", "").replace(",", "").replace(";", "")
    line = line.replace(".", "").replace(":", "").replace("«", "").replace("(", "")
    line = line.replace(")", "").replace("»", "").lower()
    print(line, file=fout, end='')
    lines_in_original_file += 1

fin.close()
fout.close()
print('***Текст успешно изменен***')
dic = open("odict.csv")  # Словарь словоформ
full_text = open("text_without_signs.txt")  # Файл с текстом после lower и удаления знаков
dic1 = open("dict1.txt")  # Словарь из задания


new_dic = []  # Словарь словообразований
for line in dic:
    new_dic.append(line)

text = []  # Текст без знаков
for line in full_text:
    text.append(line.split())

new_dic1 = dict()  # Словарь
for line in dic1:
    line = line.split()
    new_dic1[line[0]] = line[1]
print(new_dic1)
words = unique_count(text)
print('----------------------------Подготовка и Задание 1----------------------------\n')

print('----------------------------Задание 2----------------------------')
print('Количество словоформ в тексте: ' + str(count_words(text)))
print('Количество разных словоформ: ' + str(len(words)))
print('Словоформ в словаре: ' + str(words_in_dic(words)))

'''
Также по ошибке была сделана лишняя работа по подсчету "словообразований".
Для примера, в тексте: "Я видел птицу которая видела птиц которые летели на юг"
Будет 7 словообразований.
Если вам интересно, то можете скачать словарь словоформ - http://odict.ru/ и проверить.
'''
# word_forms(new_dic)
print('----------------------------Задание 2----------------------------\n')

print('----------------------------Задание 3----------------------------')
not_in_dic = words_not_in_dic(words)
print('Количество слов не из словаря: ' + str(len(not_in_dic)))
print('Сами слова: ' + str(not_in_dic))
bad_words = find_bad_words()
print('----------------------------Задание 3----------------------------\n')

print(bad_words)  # [Оригинальное слово, надо заменить, ред. расстояние]
print(text)
for word in bad_words:  # Замена слов в тексте без знаков
    for line in text:
        for i in range(len(line)):
            if line[i] == word[0] and word[2] < 3:
                line[i] = word[1]

signs = {"!", "?", ",", ";", ".", ":", "«", "(", ")", "»", "-"}
original_text = open("brain216.txt", encoding="utf8")

for i in range(lines_in_original_file):
    line = original_text.readline().split()
    for j in range(len(line)):
        if line[j] != line[j].lower():  # Добавление заглавных букв
            text[i][j] = text[i][j].replace(text[i][j][0], line[j][0], 1)
        if line[j][-1] in signs:  # Добавление знаков
            text[i][j] = text[i][j] + line[j][-1]
print('----------------------------Задание 4----------------------------')
# Пишем исправленный текст в файл
edited_text = open('edited text.txt', 'w')
for line in text:
    for word in line:
        print(word, end=' ', file=edited_text)
    print(file=edited_text)
edited_text.close()

edited_text = open('edited text.txt')  # Открываем исправленный текст для проверки ошибок
text = []
for line in edited_text:
    text.append(line.split())
words = unique_count(text)

print('Количество словоформ в тексте: ' + str(count_words(text)))
print('Количество разных словоформ: ' + str(len(words)))
print('Словоформ в словаре: ' + str(words_in_dic(words)))
print('----------------------------Задание 4----------------------------\n')

print('----------------------------Задание 5----------------------------')
for a in bad_words:
    if a[2] > 2:
        a[1] = 'НЕ НАЙДЕНО'
        a[2] = '>2'
for a in bad_words:
    print(str(a[0]) + ' - ' + str(a[1]) + ' - ' + str(a[2]))
print('----------------------------Задание 5----------------------------')
