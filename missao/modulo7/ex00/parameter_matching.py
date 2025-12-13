#!/usr/bin/env python3

import sys

if len(sys.argv)-1 != 1:
    print("none")
else:
    parametro = sys.argv[1]
    entrada = input("What was the parameter? ")
    if entrada == parametro:
        print("Good job!")
    else:
        print("Nope, sorry...")