#!/usr/bin/env python3

def array_de_nomes(pessoas):
    lista = []
    for primeiro, ultimo in pessoas.items():
        nome_completo = f"{primeiro.capitalize()} {ultimo.capitalize()}"
        lista.append(nome_completo)
    return lista


# Teste do exemplo
pessoas = {
    "jean": "valjean",
    "grace": "hopper",
    "xavier": "niel",
    "fifi": "brindacier"
}

print(array_de_nomes(pessoas))