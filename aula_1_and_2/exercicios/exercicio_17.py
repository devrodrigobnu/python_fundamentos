    # Exercicio 17:
    # Crie um programa que solicite ao usuário que insira a 
    # quantidade de notas do aluno a serem calculadas.
    #  Em seguida, peça para o usuário digitar as notas uma por uma. 
    # Armazene essas notas em uma lista.
    # Calcule a média das notas utilizando um for loop para somar todos os 
    # elementos da lista e dividir pela quantidade de notas.
    # Verifique se a média é maior ou igual a 6.0. Se a média for maior ou igual a 6.0, 
    # exiba a mensagem "Aluno Aprovado!".
    # Caso contrário, exiba a mensagem "Aluno Reprovado!".

    #       Dicas:
    # Utilize um for loop para solicitar as notas e armazená-las na lista.
    # Use um acumulador para calcular a soma das notas e, ao final do loop, 
    # divida pela quantidade de notas para obter a média.
    # Use uma estrutura condicional (if-else) para verificar se o aluno foi aprovado ou 
    # reprovado com base na média calculada.
    # Certifique-se de converter os valores digitados pelo usuário para o tipo 
    # adequado (int ou float) ao armazená-los na lista.

import os

def obter_quantidade_notas():
    while True:
        try:
            quantidade_notas = int(input('Digite a quantidade de notas do aluno: '))
            if quantidade_notas > 0:
                return quantidade_notas
            else: 
                raise ValueError('Informe números acima de zero!')
        except Exception as e: 
            print(f'Ocorreu um erro: {str(e)}')
            print('Informe uma quantidade válida!')
        

def obter_notas(quantidade_notas):
    lista_notas = []

    while len(lista_notas) < quantidade_notas:
        try:
            nota = float(input(f'Informe a {len(lista_notas) + 1}º uma nota: '))

            if nota >= 0 and nota <= 10:
                lista_notas.append(nota)

        except Exception as e:
            print(f'Ocorreu um erro: {str(e)}')
            print(f'Informe uma nota válida!')

    return lista_notas

def calcular_media_notas(lista_notas):
    soma = 0
    for nota in lista_notas:
        soma += nota
    media = soma / len(lista_notas)
    return media
        

def exibir_resultado(media):
    print('A média é:', media)
    if media >= 6.0:
        print('O aluno está aprovado!')
    else: 
        print('O aluno está reprovado!')

def main():
    quantidade = obter_quantidade_notas()
    notas = obter_notas(quantidade)
    media_calculada = calcular_media_notas(notas)
    exibir_resultado(media_calculada)


if __name__ == '__main__':
    os.system('cls')
    main()