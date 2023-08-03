# Exercicio 15:
# Crie uma função que solicite ao usuário que insira uma lista de notas de alunos 
# (números reais entre 0 e 10).
# A função deve calcular e exibir a média, a nota mais alta e a nota mais baixa. 
# Utilize listas e for loops para
# processar as notas digitadas pelo usuário.

import os

def recebe_notas_alunos():
    notas = []
    while True:
        nota_str = input('Insira a nota do aluno ou digite sair para encerrar: ')
        
        if nota_str.lower() == 'sair':
            break
        
        try:
            nota = float(nota_str)
            if 1 <= nota <= 10:
                notas.append(nota)
            else:
                print('Nota fora do intervalo permitido (1 a 10).')
        except:
            print('Valor inválido. Insira um número válido ou sair para encerrar!')
    return notas


def calcular_media_notas():
    ...

def exibir_media_notas():
    ...








def main():
    notas_alunos = recebe_notas_alunos()
    print('Notas dos alunos:', notas_alunos)
    

if __name__ == '__main__':
    os.system('cls')
    main()