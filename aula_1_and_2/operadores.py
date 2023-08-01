import os

def verifica_numeros():
    try: 
        primeiro_numero = int(input('Digite o primeiro número: '))
        segundo_numero = int(input('Digite o segundo número: '))

        if primeiro_numero > 0 and segundo_numero > 0:
            if primeiro_numero != segundo_numero:
                if primeiro_numero > segundo_numero:
                    print('Primeiro número é maior que o segundo número!')
                elif primeiro_numero < segundo_numero:
                    print('Primeiro número é menor que o segundo número!')
            elif primeiro_numero == segundo_numero:
                print('Números são iguais!')

        else:
            print('Números precisam ser positivos!')


    except:
        print('Erro ao converter os dados para int!')

def verifica_idade():
    try:
        idade_usuario = int(input('Informe a sua idade: '))
        if idade_usuario > 0 and idade_usuario < 120:
            # Verificar se é adulto(a) e para isso
            # precisa ter 18 anos ou mais
            if idade_usuario >= 18:
                print('Você é um adulto(a)')
            elif idade_usuario >= 12 and idade_usuario < 18:
                print('Você é um adolescente!')
            elif idade_usuario < 12:
                print('Você é uma criança!')
        else: 
            print('Idade inválida!')
    except:
        print('Erro ao ler dados!')

if __name__ == '__main__':
    os.system('cls')
    os.system('python --version')
    verifica_numeros()
    verifica_idade()