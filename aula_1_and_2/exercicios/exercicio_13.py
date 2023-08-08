# Exercicio 13:
# Crie uma função que remova as duplicatas de uma lista de números. 
# Por exemplo, se a lista for [1, 2, 2, 3, 4, 4, 5],
# o programa deve retornar a lista sem duplicatas: [1, 2, 3, 4, 5]. 
# Utilize listas e um for loop para percorrer a lista
# original e uma nova lista para armazenar os elementos únicos.

import os

def recebe_lista():
    lista_dados = [
        1, 2, 3,
        3, 3, 5,
        5, 6, 6,
        7, 7, 7,
        8, 9, 10,
        11, 11, 11,
    ]
    return lista_dados

def remover_duplicados(lista_dados):
    lista_sem_duplicidade = []

    for item in lista_dados:
        contador = 0
        for item_2 in lista_dados:
            if item == item_2:
                contador += 1

        if contador == 1:
            lista_sem_duplicidade.append(item)

    return lista_sem_duplicidade

def exibir_nova_lista(lista_sem_duplicidade):
    print(lista_sem_duplicidade)



def main():
    lista_dados = recebe_lista()
    lista_sem_duplicidade = remover_duplicados(lista_dados)
    exibir_nova_lista(lista_sem_duplicidade)




if __name__ == '__main__':
    os.system('cls')
    main()