# Exercício 2:
# Crie uma função que receba uma lista de números e retorne a soma de todos os elementos da lista.

import os

def retornar_soma():
    lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    soma = sum(lista)
    return soma

resultado = retornar_soma()
print(f'A soma da lista é: {resultado}')


if __name__ == '__main__':
    retornar_soma()