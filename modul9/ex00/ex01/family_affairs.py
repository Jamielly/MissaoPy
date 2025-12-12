#!/usr/bin/env python3

def find_the_redheads(familia):
    vermelhos = filter(lambda nome: familia[nome] == "red", familia.keys())
    return list(vermelhos)


# Teste do exemplo
familia_dupont = {
    "florian": "red",
    "marie": "blond",
    "virginie": "brunette",
    "david": "red",
    "franck": "red"
}

print(find_the_redheads(familia_dupont))
