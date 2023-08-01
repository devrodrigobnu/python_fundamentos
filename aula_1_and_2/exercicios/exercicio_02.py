#   Exercicio 2:
# 	Escreva uma função que calcule a média de três notas fornecidas pelo usuário e
# 	armazene o resultado em uma variável. Em seguida, exiba a média calculada no terminal.

import os

def media():
    while True:
        try:
            nota_1 = float(input('Digite a primeira nota: '))
            nota_2 = float(input('Digite a segunda nota: '))
            nota_3 = float(input('Digite a terceira nota: '))
            media = (nota_1 + nota_2 + nota_3) / 3
            if nota_1 > 0 and nota_1 <= 10 and nota_2 > 0 and nota_2 <= 10 and nota_3 > 0 and nota_3 <= 10:
                break
        except:
            print('Digite um número válido!')
    print(f'A média das 3 notas é: {media}')

if __name__ == '__main__':
    os.system('cls')
    media()