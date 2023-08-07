# Exercicio 11:
# Crie uma função que solicite ao usuário que insira uma 
# sequência de números inteiros separados por espaço e,
# em seguida, calcule e exiba a média desses números. 
# Utilize listas para armazenar os números digitados pelo usuário
# e um for loop para calcular a soma dos elementos da lista.

import os

def recebe_numeros_usuario():
    numeros = input('Digite os números inteiros separados por espaço: ')
    numeros_lista = [int(num) for num in numeros.split()]
    return numeros_lista
    
def calcula_media_numero(numeros):
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

def exibe_calculo_media(media):
    print('A média é:', media)

def main():
    numeros = recebe_numeros_usuario()
    media = calcula_media_numero(numeros)
    exibe_calculo_media(media)


if __name__ == '__main__':
    os.system('cls')
    main()  