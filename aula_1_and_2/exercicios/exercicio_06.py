# Exercicio 6:
# Crie uma função que pergunte ao usuário quais são seus três filmes favoritos e 
# armazene cada filme em uma lista.
# Depois mostre esses items usando um for, com uma função distinta que 
# recebe uma lista por parâmetro e mostra seus items.


import os


def filmes_favoritos():
    lista_filmes = []
    for i in range(3):
        item = input(f'Informe o {i + 1}º filme favorito: ')
        lista_filmes.append(item)

    print('\nFilmes favoritos informados pelo usuário: ')
    for item in lista_filmes:
        print(item)



if __name__ == '__main__':
    os.system('cls')
    filmes_favoritos()