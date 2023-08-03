# Exercicio 5:
# Crie uma função que solicite ao usuário que insira seu endereço completo 
# (incluindo rua, número, bairro, cidade e CEP) e armazene as informações em variáveis separadas.
# Depois mostre essas informações usando concatenação com uma mensagem.

import os



def receba_dados_endereco():
    while True:
        try:
            numero = int(input('Informe o número da residência: '))
            rua = input('Informe o nome da rua: ')
            bairro = input('Informe o bairro: ')
            cidade = input('Informe o nome da cidade: ')
            cep = input('Digite o cep da residência: ')
            return numero, rua, bairro, cidade, cep
        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')

def mostra_dados_endereco(numero, rua, bairro, cidade, cep):
    print(f'O endereço informado é {rua} - {numero}, {bairro}, {cidade}, {cep}')

def main():
    numero, rua, bairro, cidade, cep = receba_dados_endereco()
    mostra_dados_endereco(numero, rua, bairro, cidade, cep)

if __name__ == '__main__':
    os.system('cls')
    main()