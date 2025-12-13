#!/usr/bin/env python3

import sys 

args = sys.argv[1:]

if len(args) == 0:
    print("none")
    exit()

for palavra in args:
    if not palavra.endswith("ism"):
        print(palavra + "ism")
