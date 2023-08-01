# Exercicio 10:
# Dado um número inteiro positivo N, crie uma função que exiba todos os números pares de 0 até N (inclusive).
# Utilize um for loop para alterar pelos números e um operador de módulo (%) para verificar se o número é par.

import os

def exibir_numero_par(N):
    for numero in range(N + 1):
        if numero % 2 == 0:
            print(numero)

if __name__ == '__main__':
    os.system('cls')
    numero_inteiro = 10
    exibir_numero_par(numero_inteiro)