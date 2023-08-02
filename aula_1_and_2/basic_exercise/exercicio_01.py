# Exercício 1:
# Crie uma função que receba um número inteiro e verifique se ele é par ou ímpar. 
# A função deve retornar True se o número for par e False se for ímpar.

import os

def filtrar_par_impar(numero):
    if numero % 2 == 0:
        return True
    else:
        return False

num = int(input('Digite um número inteiro: '))
resultado = filtrar_par_impar(num)

if resultado:
        print(f'O número {num}, é par')
else:
        print(f'O número {num}, é ímpar')   

if __name__ == '__main':
    os.system('cls')
    filtrar_par_impar()


