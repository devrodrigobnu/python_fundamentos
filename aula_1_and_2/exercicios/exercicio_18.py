# Crie uma função que exiba uma mensagem perguntando a idade do usuário e, com base na idade fornecida,
# 	exiba diferentes mensagens de acordo com as seguintes faixas etárias: 
# 0-12 anos, 13-17 anos, 18 ou mais anos.
# 	(mais faixas etárias podem ser incluídas)

import os

def exiba_faixa_etaria():
    idade = 0
    while True:
        try:
            idade = int(input('Informa a idade: '))
            break
        except:
            print('Informe uma idade válida')

    if idade <= 12:
        print('Criança')
    elif idade < 18:
        print('Teen!')
    else:
        print('Adulto!')

if __name__ == '__main__':
    exiba_faixa_etaria()