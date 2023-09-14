# IF e ELSE -> utiliza de operadores relacionais para exibir ou executar o código
# Switch Case -> Definida que entra em uma estrutura de caso

# For -> é uma estrutura de repetição que é composta por indice
# While -> é uma estrutura de repetição que é baseada em operadores relacionais

# chave e valor
nome = input('Digite seu nome >> ')
idade = int(input('Digite sua idade >> '))

nota1 = float(input('Digite sua nota >> '))
nota2 = float(input('Digite sua nota >> '))
# Procedencia aritimética
media = (nota1 + nota2) / 2

aluno = {
    'Nome': nome,
    'Idade': idade,
    'Nota1': nota1,
    'Nota2': nota2,
    'Media': media
}

condicional = int(input(
""" Digite o número que representa a característica que deseja saber
\n1- Nome
\n2- Idade
\n3- Primeira nota
\n4- Segunda nota
\n5- Média
\n >>>>> """
))


if condicional == 1:
    print(f'O nome do aluno é {aluno["Nome"]}')
elif condicional == 2:
    print(f'O nome do aluno é {aluno["Idade"]}')
elif condicional == 3:
    print(f'A primeira nota do aluno é {aluno["Nota1"]}')
elif condicional == 4:
    print(f'A segunga nota do aluno é {aluno["Nota2"]}')
elif condicional == 5:
    print(f'A média do aluno é {aluno["Media"]}')
else:
    print('Você digitou um número inválido.')