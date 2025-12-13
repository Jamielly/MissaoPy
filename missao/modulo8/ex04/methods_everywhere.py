#!/usr/bin/env python3

import sys

def shrink(texto):
    print(texto[:8])

def enlarge(texto):
    while len(texto) < 8:
        texto += "Z"
    print(texto)

args = sys.argv[1:]

if len(args) == 0:
    print("none")
    exit()

for item in args:
    tamanho = len(item)

    if tamanho > 8:
        shrink(item)
    elif tamanho < 8:
        enlarge(item)
    else:
        print(item)
