#   Exercicio 2:
# 	Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
# 	armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os

def calcula_media(lista_notas) -> float:
    soma_das_notas = 0
    for nota in lista_notas:
        soma_das_notas += nota
    
    media_notas = soma_das_notas / len(lista_notas)
    return media_notas

def recebe_dados() -> list:
    lista_notas = []
    while len(lista_notas) < 3 :
        try:
            nota = float(input('Informe a nota: '))
            if nota > 0 and nota <= 10:
                lista_notas.append(nota)
                print(f'Adicinou nota: {nota}, com sucesso!')
        except:
            print('Informe uma nota válida!')

    return lista_notas


def mostrar_resultado(media_notas) -> None:
    print(f'A média das notas é: {media_notas}!')




if __name__ == '__main__':
    os.system('cls')
    lista_notas = recebe_dados()
    media_notas = calcula_media(lista_notas)
    mostrar_resultado(media_notas)
