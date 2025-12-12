#!/usr/bin/env python3

def add_one(x):
    return x + 1

numero = 5
print(numero)      # valor original

add_one(numero)    # isso NÃO altera "numero" no escopo externo

print(numero)      # continua igual!
