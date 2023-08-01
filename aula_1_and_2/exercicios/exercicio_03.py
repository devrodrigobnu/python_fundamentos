# Exercicio 3:
# Crie uma função que peça ao usuário que digite um número inteiro e, em seguida,
# armazene esse valor em uma variável. Crie mais funções para o usuário também informar 
# dados do tipo float e string, e armazene todos os dados em variáveis. Em seguida
# adicione todos esses items em uma lista e mostre os item através de um laço de repetição for.

import os

def user():
    lista_dados = []

    numero_inteiro = int(input('Digite um número inteiro: '))
    lista_dados.append(numero_inteiro)
    
    numero_float = float(input('Digite um número float: '))
    lista_dados.append(numero_float)

    texto = input('Digite um texto: ')
    lista_dados.append(texto)

    print('Dados armazenados na lista:')
    for item in lista_dados:
        print(item)

if __name__ == '__main__':
    os.system('cls')
    user()