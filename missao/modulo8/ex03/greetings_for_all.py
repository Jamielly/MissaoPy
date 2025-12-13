#!/usr/bin/env python3

def greetings(nome="noble stranger"):

    if not isinstance(nome, str):
        print("Error! It was not a name.")
    else:   
        print(f"Hello, {nome}.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)