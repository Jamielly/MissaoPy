#!/usr/bin/env python3

tab = 0

while tab <= 10:
    
    print(f"Table of {tab}: ", end="")
    cont = 0
    while cont <= 10:
        result =  tab * cont
        print(f"{result}", end=" ")
        cont += 1
    tab += 1
    print()
