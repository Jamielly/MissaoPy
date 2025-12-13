#!/usr/bin/env python3

import sys

if len(sys.argv) != 3:
    print("none")
    exit()

inicio = int(sys.argv[1])
fim = int(sys.argv[2])

if inicio >= fim:
    print("none")
    exit()

lista = list(range(inicio, fim + 1))
print(lista)