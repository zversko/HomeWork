# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. 
# Входные и выходные данные хранятся в отдельных текстовых файлах.

def read_string(file):       # Считывание строки из файла
    file = open(file, "r")
    s = file.readline()
    file.close()
    return s

def encoding(s):            # Кодирование строки
    encoding_string = ''
    count = 1
    for i in range(1, len(s)):
        if s[i] == s[i-1] and i != (len(s)-1):
            count += 1
        else:
            encoding_string += str(count) + str(s[i-1])
            count = 1

    return encoding_string

def decoding(s):            # Декодирование строки
    decoding_string = ''
    count = ''
    for i in range(0, len(s) - 1):
        if s[i].isdigit():
            count += s[i]
        else:
            print(count)
            decoding_string += s[i] * int(count)
            count = ''

    return decoding_string

def main():
    data = read_string('file.txt')
    print(data)
    encoding_data = encoding(data)
    print(encoding_data)
    with open('file_en.txt', 'w', encoding='utf-8') as file:
        file.write(encoding_data + '\n')

    data2 = read_string('file2.txt')
    print(data2)
    decoding_data = decoding(data2)
    print(decoding_data)
    with open('file_de.txt', 'w', encoding='utf-8') as file:
        file.write(decoding_data + '\n')

main()