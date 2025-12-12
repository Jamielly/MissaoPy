#Cada entrada do dicionário é outro dicionário:
#"ada": { "name": "Ada Lovelace", "date_of_birth": "1815" }

#!/usr/bin/env python3

def famous_births(pessoas):
    # Ordenar por ano de nascimento (convertendo ano para int)
    ordenadas = sorted(
        pessoas.values(),
        key=lambda item: int(item["date_of_birth"])
    )

    # Exibir do mais velho para o mais novo
    for pessoa in ordenadas:
        print(f'{pessoa["name"]} is a great scientist born in {pessoa["date_of_birth"]}.')


# Teste do exemplo
women_scientists = {
    "ada": { "name": "Ada Lovelace", "date_of_birth": "1815" },
    "cecilia": { "name": "Cecila Payne", "date_of_birth": "1900" },
    "lise": { "name": "Lise Meitner", "date_of_birth": "1878" },
    "grace": { "name": "Grace Hopper", "date_of_birth": "1906" }
}

famous_births(women_scientists)
