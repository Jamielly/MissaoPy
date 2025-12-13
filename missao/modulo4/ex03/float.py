#!/usr/bin/env python3

entrada = float(input("Me dê um número: "))

if entrada.is_integer():
    print("Este número é um inteiro.")
else:
    print("Este número é um decimal.")