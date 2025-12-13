#!/usr/bin/env python3

def find_the_redheads(dupont_family):
    vermelhos = filter(lambda nome: dupont_family[nome] == "red", dupont_family.keys())
    return list(vermelhos)


dupont_family = {
"florian": "red",
"marie": "blond",
"virginie": "brunette",
"david": "red",
"franck": "red"
}
print(find_the_redheads(dupont_family))