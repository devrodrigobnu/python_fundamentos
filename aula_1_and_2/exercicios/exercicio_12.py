
# # Exercicio 12:
# Crie um jogo em que o computador escolhe um número 
# aleatório entre 1 e 100, e o usuário deve adivinhar qual é esse número.
# O programa deve fornecer dicas se o número fornecido pelo usuário é maior 
# ou menor que o número escolhido pelo computador.
# Utilize um while loop para continuar o jogo até que o usuário acerte o número. 

import os
import random

def recebe_numero_aleatorio():
    numero_random = random.randint(1, 100)
    return numero_random


def escolher_numero_usuario():
    while True:
        try:
            numero_usuario = int(input('Jogo de adivinhação, digite um número entre 1 e 100: '))
            if 1 <= numero_usuario <= 100:
                return numero_usuario
            else:
                print('Digite um número válido entre 1 e 100!!')
        except:
            print('Dados inválidos!!!')  


def dicas_computador(numero_random, tentativa):
    if tentativa < numero_random:
        return 'Tente um número maior!'
    elif tentativa > numero_random:
        return 'Tente um número menor!'
    

def exibir_vitoria_usuario(tentativas):
    print(f'Parabéns! Você adivinhou o número correto em {tentativas} tentativas. Você venceu!')


def main():
    numero_aleatorio = recebe_numero_aleatorio()
    tentativas = 0

    while True:
        tentativa = escolher_numero_usuario()
        tentativas += 1
        
        if tentativa == numero_aleatorio:
            exibir_vitoria_usuario(tentativas)
            break
        else: 
            dica = dicas_computador(numero_aleatorio, tentativa)
            print(dica)

if __name__ == '__main__':
    os.system('cls')
    main()