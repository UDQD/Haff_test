from haff import *
# import ast.literal_eval()
import json


def main():
    h = Haff()
    ch = input('1 - encode, 0 - decode: ')
    if ch == '1':
        s = input('===>')  # читаем строку длиной  до 10**4
        code = h.huffman_encode(s)  # кодируем строку
        encoded = "".join(code[ch] for ch in s)  # отобразим закодированную версию, отобразив каждый символ
        # в соответствующий код и конкатенируем результат
        print(len(code), len(encoded))  # выведем число символов и длину закодированной строки
        # for ch in sorted(code):  # обойдем символы в словаре в алфавитном порядке с помощью функции sorted()
        #     print("{}: {}".format(ch, code[ch]))  # выведем символ и соответствующий ему код
        print(code)
        print(encoded)  # выведем закодированную строку
    else:
        s = input('str: ')
        c = input('code: ')
        a = json.loads(c.replace("'", '"'))
        decoded = h.huffman_decode(s, a)
        print(decoded)

        # {'2': '00', '3': '01', '1': '1'}
        # 10001111


if __name__ == "__main__":
    main()
