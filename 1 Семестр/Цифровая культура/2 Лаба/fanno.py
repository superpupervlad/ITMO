from collections import Counter


def divide_table(table):
    optimal_difference = sum(table.values())
    optimal_index = 0

    for i in range(len(table)):
        current_difference = abs(sum(list(table.values())[:i]) - sum(list(table.values())[i:]))

        if current_difference < optimal_difference:
            optimal_difference = current_difference
            optimal_index = i
    return dict({item for i, item in enumerate(table.items()) if i < optimal_index}), \
           dict({item for i, item in enumerate(table.items()) if i >= optimal_index})


def shenon_get_codes(table, value='', codes={}):
    if len(table) != 1:
        a, b = divide_table(table)
        shenon_get_codes(a, value + '0', codes)
        shenon_get_codes(b, value + '1', codes)
    else:
        codes[table.popitem()[0]] = value
    return codes


def decode_symbol(table, code, index=0):
    if len(table) != 1:
        a, b = divide_table(table)
        if code[index] == '0':
            return decode_symbol(a, code, index + 1)
        else:
            return decode_symbol(b, code, index + 1)
    else:
        return table.popitem()[0]

data = input('Шифруемая строка: ')
counter = Counter(data)

# Символы первичного алфавита по убыванию вероятностей.
sorted_freq = sorted(set(data), key=lambda letter: counter[letter], reverse=True)
sorted_freq_dict = {letter: counter[letter] for letter in sorted_freq}

code_table = shenon_get_codes(sorted_freq_dict)  # таблица символов со значениями частоты

print(sorted_freq_dict)
for symbol, key in sorted(code_table.items(), key=lambda item: len(item[1])):
    print(symbol, key, sep=': ')

encoded = [code_table[letter] for letter in data]
encoded_bits = ''.join(encoded)
encoded_str = [chr(int(encoded_bits[i:i + 8], 2)) for i in range(0, len(encoded_bits), 8)]

print('исходная строка ({} bits): '.format(len(data) * 8), data)
print('сжатая строка ({} bits): '.format(len(encoded_str) * 8), ''.join(encoded_str))
print('данные: {}'.format(encoded_bits))

index = 0
decoded_str = ''

while index < len(encoded_bits):
    current = decode_symbol(sorted_freq_dict, encoded_bits, index)  # расшифровать очередной символ
    decoded_str += current             # добавить его в результат
    index += len(code_table[current])  # перейти на следующий

print('расшифрованная строка: ', decoded_str)