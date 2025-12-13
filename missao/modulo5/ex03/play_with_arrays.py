#!/usr/bin/env python3

orig = [2, 8, 9, 48, 8, 22, -12, 2]
new = []

for i in orig:
    if i > 5: 
        new.append(i + 2)
        new_set = set(new)

print(f"{orig}")
print(f"{new_set}")

