#!/usr/bin/env python3

import sys
import re

if len(sys.argv) > 2:
        chave = sys.argv[1]
        pesquisa = sys.argv[2]
        result = re.findall(chave, pesquisa).count(chave)

        if result == 0:
            print("none")
        else: 
             print(result)
else:
    print("none")