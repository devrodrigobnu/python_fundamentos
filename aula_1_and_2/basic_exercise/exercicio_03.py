# Exercício 3:
# Crie uma função que receba uma lista de números e retorne o produto(multiplicação) de todos os 
# elementos da lista.

import os

def calcular_produto(lista_numeros):
    produto = 1
    for num in lista_numeros:
        produto *= num
    return produto

lista_numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
resultado = calcular_produto(lista_numeros)
print(f'O produto dos números é: {resultado}')


if __name__ == '__main__':
    calcular_produto(lista_numeros)