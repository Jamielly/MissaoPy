#!/usr/bin/env python3

import sys 

if len(sys.argv) != 2:
    print("none")
    exit()

texto = sys.argv[1]
resultado = ""

for char in texto:
    if char == "z":
        resultado += "z"

if resultado == "":
    print("none")
else:
    print(resultado)