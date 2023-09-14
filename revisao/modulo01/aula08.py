# chave e valor
nome = input('Digite seu nome >> ')
idade = int(input('Digite sua idade >> '))

nota1 = float('Digite sua nota >> ')
nota2 = float('Digite sua nota >> ')

# Procedencia aritimética
media = (nota1 + nota2) / 2

aluno = {
    'Nome': nome,
    'Idade': idade,
    'Nota1': nota1,
    'Nota2': nota2,
    'Media': media
}

print(f'O nome do aluno é {aluno["Nome"]} e a sua média foi {aluno["Media"]}')