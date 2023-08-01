# Exercicio 8:
# Crie uma função que converta um valor em dólar para real. 
# Peça ao usuário que insira a cotação do dólar e o valor em dólar 
# a ser convertido. Em seguida, exiba o valor equivalente em reais.

import os


def converter_dolar_para_real():
    try:
        cotacao_dolar = float(input('Digite a cotação do dólar atual: '))
        valor_dolar = float(input('Digite o valor em dólar a ser convertido: '))
        valor_reais = valor_dolar * cotacao_dolar
        print(f'O valor convertido em dólar é: R${valor_reais:.2f}')
    except:
        print('Valor inválido')


if __name__ == '__main__':
    os.system('cls')
    converter_dolar_para_real()