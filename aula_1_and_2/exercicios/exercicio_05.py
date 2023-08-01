# Exercicio 5:
# Crie uma função que solicite ao usuário que insira seu endereço completo 
# (incluindo rua, número, bairro, cidade e CEP) e armazene as informações em variáveis separadas.
# Depois mostre essas informações usando concatenação com uma mensagem.

import os



def endereco():
    rua = input('Digite o nome da sua rua: ')
    numero = int(input('Digite o numero da sua casa: '))
    bairro = input('Digite o nome do seu bairro: ')
    cidade = input('Digite o nome da sua cidade: ')
    cep = int(input('Digite o seu cep: '))
    print(f'Seu endereço completo é: Rua {rua}, número {numero}, bairro {bairro}, cidade {cidade}, cep {cep}.')


if __name__ == '__main__':
    os.system('cls')
    endereco()