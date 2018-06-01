import itertools
import numpy as np
import sys

fence_iterators = (0,1,2,3,2,1)

def szyfruj():
    plain_text = str(input("Podaj wiadomość: "))
    string_len = len(plain_text)
    column = 0

    fence = np.empty((4, string_len), dtype = str)

    for c, i, v in zip(plain_text, itertools.cycle(fence_iterators), range(0, string_len)):
        fence[i, v] = c
    print(fence)

    kryptogram = ''
    for v in range(4):
        for c in range(string_len):
            kryptogram += fence[v, c]

    print(kryptogram)
    return kryptogram



def deszyfruj():
    cripto = input("Podaj szyfr: ")
    string_len = len(cripto)

    fence = np.empty((4, string_len), dtype = str)
    for i, v in zip(itertools.cycle(fence_iterators), range(0, string_len)):
        fence[i, v] = '*'

    i = 0
    decripted = ''
    for v in range(4):
        for c in range(string_len):
            if fence[v, c] == '*':
                fence[v, c] = cripto[i]
                i += 1


    for i, v in zip(itertools.cycle(fence_iterators), range(0, string_len)):
        decripted += fence[i, v]
    print("Kryptogram: " + decripted)


while 1:
    print("Zaszyfruj - 1 \nOdszyfruj - 2 \nZakończ - 0")
    try:
        opcja = int(input("Opcja: "))
        if opcja == 1:
              szyfruj()
        if opcja == 2:
            deszyfruj()
        if opcja == 0:
            sys.exit(1)
    except ValueError:
        print("\nNiepoprawna opcja. Spróbuj ponowanie\n")
        pass
