import os


def mostrar_lista():
    lista_dados = [
        1,
        2,
        3,
        'hello',
        'hi',
        False,
        True,
        1.5,
        20,
        'texto !!'
    ]

    for item in lista_dados:
        print(item)

def obter_mostrar_dados():
    lista_input = []
    for i in range(5):
        item = input(f'Informe o {i + 1}º item: ')
        lista_input.append(item)

    print('\nItens informados pelo usuários: ')
    for item in lista_input:
        print(item)    

def script_lista():
    lista_dados = []
    contador = 0

    # Receber 10 itens do usuário
    while contador < 10:
        contador += 1

        item_informado = input(f'Informe o {contador}º item: ') 
        lista_dados.append(item_informado)   

    # Mostrar os itens recebidos
    # Acessando também os indices / posicoes 
    for indice, item in enumerate(lista_dados):
        print(f'Posição {indice} - Valor {item}')


    # Loop para o usuário acessar itens específicos da lista
    while True:
        try:
            posicao_item = int(input('Informe a posição do item desejado: '))
            print(f'O item que está na posição {posicao_item} é: {lista_dados[posicao_item]}')

            verificacao = input('Informe s para parar ou informe outro valor para continuar: ')
            if verificacao == 's':
                print('Programa parou!!')
                break
        except: 
            print('Informe apenas inteiros para posiçoes em listas!!!')






if __name__ == '__main__':
    os.system('cls')
    # mostrar_lista()
    # obter_mostrar_dados()
    script_lista()

