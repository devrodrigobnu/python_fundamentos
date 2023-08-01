#   Exercicio 1:
#   Escreva uma função que solicite ao usuário que 
#   insira seu nome e, em seguida,
# 	armazene esse valor em uma variável. Em seguida, 
#   exiba uma mensagem de boas-vindas
# 	usando o nome digitado.
import os

def solicitar_usuario():
    texto_usuario = input('Informe o seu nome: ')
    print(f'Seja bem vindo {texto_usuario}')

if __name__ == '__main__':
    os.system('cls')
    solicitar_usuario()