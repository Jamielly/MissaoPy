#!/usr/bin/env python3

def array_of_names(persons):
    list = []
    for first, last in persons.items():
        nome_completo = f"{first.capitalize()} {last.capitalize()}"
        list.append(nome_completo)
    return list

persons = {
"jean": "valjean",
"grace": "hopper",
"xavier": "niel",
"fifi": "brindacier"
}
print(array_of_names(persons))