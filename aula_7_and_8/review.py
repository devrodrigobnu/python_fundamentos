import os

def eh_positivo(numero_parametro):
    if numero_parametro > 0:
        return True
    else:
        return False

def sao_numeros_iguais(numero_parametro_1, numero_parametro_2):
    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 == numero_parametro_2:
            return True
        else:
            return False
    else:
        print('Informar apenas números positivos!')


def qual_numero_eh_maior(numero_parametro_1, numero_parametro_2):
    numero_maior = None
    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 > numero_parametro_2:
            numero_maior = numero_parametro_1
        elif numero_parametro_1 < numero_parametro_2:
            numero_maior = numero_parametro_2
        else:
            print('Os números são iguais! informe números diferentes!')
    else:
        print('Informe apenas números positivos!')

    return numero_maior

def qual_numero_eh_menor(numero_parametro_1, numero_parametro_2):
    numero_menor = None
    if eh_positivo(numero_parametro_1) and eh_positivo(numero_parametro_2):
        if numero_parametro_1 < numero_parametro_2:
            numero_menor = numero_parametro_1
        elif numero_parametro_2 < numero_parametro_1:
            numero_menor = numero_parametro_2
        else:
            print('Os números são iguas! Informe números diferentes!')
    else:
        print('Informe apenas números positivos!')
    return numero_menor


def verificar_impar_par(numero_parametro_1):
    resultado = ''

    if eh_positivo(numero_parametro_1):
        if numero_parametro_1 % 2 == 0:
            resultado = 'par'
        else:
            resultado = 'impar'
    else:
        print('Informar apenas números positivos!')
    return resultado


def retorna_maior_numero_em_lista(lista_de_dados):
    maior_numero = lista_de_dados[0]
    for item in lista_de_dados:
        if item > maior_numero:
            maior_numero = item
    return maior_numero

def retorna_menor_numero_em_lista(lista_de_dados):
    maior_numero = lista_de_dados[0]
    for item in lista_de_dados:
        if item < maior_numero:
            maior_numero = item
    return maior_numero

def retorna_quantidade_de_impares_e_pares_em_lista(lista_de_dados):
    numeros_pares = 0
    numeros_impares = 0

    for numero in lista_de_dados:
        if numero % 2 == 0:
            numeros_pares += 1
        else:
            numeros_impares += 1
    return numeros_pares, numeros_impares

def rodar_calculadora(numero_1, numero_2, operacao):
    if operacao == 1:
        resultado = numero_1 + numero_2
    elif operacao == 2:
        resultado = numero_1 - numero_2
    elif operacao == 3:
        resultado = numero_1 * numero_2
    elif operacao == 4:
        if numero_2 != 0:
            resultado = numero_1 / numero_2
        else: 
            resultado = 'Divisão por zero não é permitida'
    else: 
        resultado = 'Operação não reconhecida.'
    return resultado




def main():
    menu = f'''
    \nSelecione a função:
    0 - Sair
    1 - Verificar se um número é positivo
    2 - Verificar se dois números são iguais
    3 - Verificar qual é o maior número
    4 - Verificar qual é o menor número
    5 - Verificar se é par ou ímpar
    6 - Verificar maior numero em uma lista
    7 - Verificar menor numero em euma lista
    8 - Verificar se número é par ou ímpar
    9 - Rodar a calculadora
    -> opção: '''

    while True:
        try:
            funcao_selecionada = int(input(menu))
            if funcao_selecionada == 0:
                print('O programa parou!')
                break

            elif funcao_selecionada == 1:
                numero = int(input('Informe um número: '))
                if eh_positivo(numero) is True:
                    print(f'O número {numero} é positivo')
                else:
                    print(f'o número {numero} é negativo')
            
            elif funcao_selecionada == 2:
                numero_1 = int(input('Informe o primeiro número:'))
                numero_2 = int(input('Informe o segundo número:'))

                if sao_numeros_iguais(numero_1, numero_2) is True:
                    print(f'O número {numero_1} é igual ao número {numero_2}')
                else:
                    print(f'O número {numero_1} é diferente do número {numero_2}')

            elif funcao_selecionada == 3:
                numero_1 = int(input('Digite o primeiro número: '))
                numero_2 = int(input('Digite o segundo número: '))

                numero_retornado = qual_numero_eh_maior(numero_1, numero_2)
                if numero_retornado is not None:
                    print(f'O maior número é: {numero_retornado}')

            elif funcao_selecionada == 4:
                numero_1 = int(input('Digite o primeiro número: '))
                numero_2 = int(input('Digite o segundo número: '))

                numero_retornado = qual_numero_eh_menor(numero_1, numero_2)
                if numero_retornado is not None:
                    print(f'O menor número é: {numero_retornado}')

            elif funcao_selecionada == 5:
                numero = int(input('Informe um número: '))
                resultado = verificar_impar_par(numero)

                if resultado != '':
                    print(f'O número {numero} é {resultado}')

            elif funcao_selecionada == 6:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos itens serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º ítem: '))
                        lista_de_dados.append(item)
                        contador += 1
                    except:
                        print('Informe um número válido!')

                maior_numero = retorna_maior_numero_em_lista(lista_de_dados)          
                print(f'O maior número da lista é: {maior_numero}')

            elif funcao_selecionada == 7:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos itens serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º ítem: '))
                        contador += 1
                        lista_de_dados.append(item)
                    except:
                        print('Informe um número válido!')
                menor_numero = retorna_menor_numero_em_lista(lista_de_dados)
                print(f'O menor número da lista é: {menor_numero}')
        
            elif funcao_selecionada == 8:
                lista_de_dados = []
                contador = 0
                limite = int(input('Informe quantos itens serão inseridos: '))

                while contador < limite:
                    try:
                        item = int(input(f'Informe o {contador + 1}º ítem: '))
                        contador += 1
                        lista_de_dados.append(item)
                    except:
                        print('Informe um número válido!')
                pares, impares = retorna_quantidade_de_impares_e_pares_em_lista(lista_de_dados)
                print('Itens da lista:', lista_de_dados)
                print(f'Quantidade de pares: {pares}')
                print(f'Quantidade de impares: {impares}')

            elif funcao_selecionada == 9:

                menu_operacoes = '''
                \nOperações:
                1- Somar
                2- Subtrair
                3- Multiplicar
                4- Dividir
                ->Opção: '''
                numero_1 = int(input('Digite o primeiro número: '))
                numero_2 = int(input('Digite o segundo número: '))
                while True:
                    try:
                        operacao = int(input(menu_operacoes))

                        if operacao in [1, 2, 3, 4]:
                            resultado = rodar_calculadora(numero_1, numero_2, operacao)
                            print('Resultado:', resultado)
                            break
                        else:
                            print('Informe uma operação válida!')
                    except:
                        print('Informe um número válido!')


        except Exception as e:
            print(f'Erro: {e}')

if __name__ == '__main__':
    main()
