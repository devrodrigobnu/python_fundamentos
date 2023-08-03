
# # Exercicio 16:
# Crie uma função que receba uma lista de palavras e um determinado 
# caractere. O programa deve exibir todas as
# palavras que contêm o caractere fornecido pelo usuário. 
# Utilize listas, for loops e operadores para realizar a busca.

import os

def recebe_lista_palavras(lista, caractere):
    palavras_com_caracter = []
    for palavra in lista:
        if caractere in palavra:
            palavras_com_caracter.append(palavra)   
    return palavras_com_caracter

def exibir_palavras(palavras, caractere):
    if palavras:
        print(f'Palavras que contêm o caractere {caractere}')
        for palavra in palavras:
            print(palavra)
    else:
            print('Não foram encontradas palavras com o caractere fornecido')

def main():
    while True:
        lista_palavras = input('Digite uma lista de palavras separadas por espaço: ').split()
        caractere = input('Digite um caractere: ')
        palavras_com_caractere = recebe_lista_palavras(lista_palavras, caractere)
        exibir_palavras(palavras_com_caractere, caractere)
        continuar = input('Deseja continuar? (s/n)')
        if continuar.lower() != 's':
            break
if __name__ == '__main__':
    os.system('cls')
    main()