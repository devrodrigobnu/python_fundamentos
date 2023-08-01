# Exercicio 9:
# Crie uma função que converta um valor em horas para minutos e segundos. 
# Solicite ao usuário que digite o valor em horas e, em seguida, exiba as 
# conversões para minutos e segundos.
# Fórmula para converter horas em minutos: Minutos = Horas * 60
# Fórmula para converter horas em segundos: Segundos = Horas * 3600

import os

def converter_hora():
    try:
        horas = float(input('Digite o valor em horas a ser convertido: '))
        minutos = horas * 60
        segundos = horas * 3600
        print(f'O valor convertido em miuntos é: {minutos} e em segundos é: {segundos}')
    except:
        print('Digite um valor válido!')


if __name__ == '__main__':
    os.system('cls')
    converter_hora()