#!/usr/bin/env python3

def add_one(num):
    num = num + 1
    
entrada = 5
print(entrada)      # valor original

add_one(entrada)    # isso NÃO altera no escopo externo

print(entrada)      # continua igual!