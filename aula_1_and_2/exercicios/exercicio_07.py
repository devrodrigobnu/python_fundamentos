# Exercicio 7:
# Crie uma função que solicite ao usuário que insira a data de nascimento no formato "dd/mm/aaaa" e armazene o dia,
# mês e ano em variáveis diferentes. Mostre uma mensagem com as variáveis separadas.
import os



def obter_data_nascimento():
    data_nascimento = input('Insira sua data de nascimento no formato dd/mm/yyyy: ')
    dia, mes, ano = data_nascimento.split('/')

    print('Dia:', dia)
    print('Mês:', mes)
    print('Ano:', ano)



if __name__ == '__main__':
    os.system('cls')
    obter_data_nascimento()