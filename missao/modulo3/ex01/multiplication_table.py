#!/usr/bin/env python3

print("Enter a number")
i = int(input())

j = 0
while j <= 10:
    result = j * i 
    print(f"{j} x {i} = {result}")
    j += 1