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
    return int(input('Digite a quantidade de notas do aluno: '))

def obter_notas(quantidade_notas):
    notas = []
    for i in range(quantidade_notas):
        nota = float(input(f'Digite a nota {i + 1}: '))
        notas.append(nota)
    return notas


def calcular_media_notas(notas):
    soma = 0
    for valor in notas:
        soma += valor
    media = soma / len(notas)
    return media
    

def exibir_resultado(media):
    print('A média é:', media)
    if media == 6.0:
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