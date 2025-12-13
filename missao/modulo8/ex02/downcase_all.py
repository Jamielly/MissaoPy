#!/usr/bin/env python3

import sys

def downcase_all(texto):
    return texto.lower()

args = sys.argv[1:]

if len(args) == 0:
    print("none")
    exit()

for item in args:
    print(downcase_all(item))